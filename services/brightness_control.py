import platform
import subprocess
import os


def get_current_brightness():
    """
    Get the current screen brightness level as a percentage (0-100)

    Returns:
        int: Current brightness percentage
    """
    system = platform.system()

    if system == "Windows":
        try:
            import wmi

            c = wmi.WMI(namespace="wmi")
            brightness = c.WmiMonitorBrightness()[0].CurrentBrightness
            return brightness
        except ImportError:
            try:
                import ctypes

                class DISPLAY_DEVICE(ctypes.Structure):
                    _fields_ = [
                        ("cb", ctypes.c_ulong),
                        ("DeviceName", ctypes.c_char * 32),
                        ("DeviceString", ctypes.c_char * 128),
                        ("StateFlags", ctypes.c_ulong),
                        ("DeviceID", ctypes.c_char * 128),
                        ("DeviceKey", ctypes.c_char * 128),
                    ]

                # Placeholder for actual brightness retrieval
                return 50  # Default midpoint
            except Exception:
                return 50  # Default midpoint

    elif system == "Darwin":  # macOS
        try:
            result = subprocess.run(
                [
                    "osascript",
                    "-e",
                    'tell application "System Events"\n'
                    "    get the brightness of the first display\n"
                    "end tell",
                ],
                capture_output=True,
                text=True,
            )
            return int(float(result.stdout.strip()) * 100)
        except Exception:
            return 50  # Default midpoint

    elif system == "Linux":
        try:
            # For systems using xrandr
            result = subprocess.run(
                ["xrandr", "--prop"], capture_output=True, text=True
            )
            for line in result.stdout.split("\n"):
                if "Brightness:" in line:
                    return int(float(line.split(":")[1].strip()) * 100)
            return 50  # Default midpoint
        except Exception:
            return 50  # Default midpoint

    return 50  # Default midpoint if detection fails


def set_screen_brightness(value):
    """
    Set the screen brightness to a specific percentage

    Args:
        value (int): Target brightness percentage (0-100)

    Returns:
        bool: True if successful, False otherwise
    """
    system = platform.system()
    normalized_value = max(0, min(100, value))  # Ensure value is between 0-100

    if system == "Windows":
        try:
            import wmi

            c = wmi.WMI(namespace="wmi")
            c.WmiMonitorBrightnessMethods()[0].WmiSetBrightness(normalized_value, 0)
            return True
        except ImportError:
            # Fallback Windows method (requires admin rights)
            try:
                os.system(
                    f"powercfg /setacvalueindex SCHEME_CURRENT SUB_VIDEO VIDEOIDLE {normalized_value}"
                )
                os.system("powercfg /setactive SCHEME_CURRENT")
                return True
            except Exception:
                return False

    elif system == "Darwin":  # macOS
        try:
            # Convert percentage to decimal for macOS
            brightness_decimal = normalized_value / 100.0
            subprocess.run(
                [
                    "osascript",
                    "-e",
                    f'tell application "System Events"\n'
                    f"    set the brightness of the first display to {brightness_decimal}\n"
                    f"end tell",
                ],
                check=True,
            )
            return True
        except Exception:
            return False

    elif system == "Linux":
        try:
            # For systems using xrandr
            displays = subprocess.check_output(["xrandr"]).decode().split("\n")
            connected_displays = [
                line.split()[0] for line in displays if " connected" in line
            ]

            for display in connected_displays:
                brightness_decimal = normalized_value / 100.0
                subprocess.run(
                    [
                        "xrandr",
                        "--output",
                        display,
                        "--brightness",
                        str(brightness_decimal),
                    ],
                    check=True,
                )
            return True
        except Exception:
            return False

    return False  # Unsupported system or failed to set brightness


def increase_brightness(increment=10):
    """
    Increase screen brightness by the specified increment

    Args:
        increment (int): Amount to increase brightness (default: 10%)

    Returns:
        tuple: (success, new_brightness, message)
    """
    try:
        current_brightness = get_current_brightness()
        new_brightness = min(
            current_brightness + increment, 100
        )  # Increase by increment%, max 100%
        success = set_screen_brightness(new_brightness)
        if success:
            return True, new_brightness, f"Brightness increased to {new_brightness}%"
        else:
            return False, current_brightness, "Unable to adjust brightness"
    except Exception as e:
        return False, 0, f"Error: {str(e)}"


def decrease_brightness(decrement=10):
    """
    Decrease screen brightness by the specified decrement

    Args:
        decrement (int): Amount to decrease brightness (default: 10%)

    Returns:
        tuple: (success, new_brightness, message)
    """
    try:
        current_brightness = get_current_brightness()
        new_brightness = max(
            current_brightness - decrement, 0
        )  # Decrease by decrement%, min 0%
        success = set_screen_brightness(new_brightness)
        if success:
            return True, new_brightness, f"Brightness decreased to {new_brightness}%"
        else:
            return False, current_brightness, "Unable to adjust brightness"
    except Exception as e:
        return False, 0, f"Error: {str(e)}"
