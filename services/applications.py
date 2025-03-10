# services/application_service.py

import subprocess
import winreg
import pyautogui


class ApplicationService:
    def __init__(self):
        self.common_apps = {
            "notepad": "notepad.exe",
            "calculator": "calc.exe",
            "paint": "mspaint.exe",
            "word": "winword.exe",
            "excel": "excel.exe",
            "powerpoint": "powerpnt.exe",
            "chrome": "chrome.exe",
            "firefox": "firefox.exe",
            "explorer": "explorer.exe",
        }

    def get_app_path(self, app_name):
        try:
            key = winreg.OpenKey(
                winreg.HKEY_LOCAL_MACHINE,
                r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\\" + app_name,
            )
            return winreg.QueryValue(key, None)
        except WindowsError:
            return None

    def open_application(self, app_name):
        app_name = app_name.lower()

        if app_name in self.common_apps:
            app_executable = self.common_apps[app_name]
            app_path = self.get_app_path(app_executable)
            if app_path:
                subprocess.Popen(app_path)
                return f"Opening {app_name}"
            else:
                try:
                    subprocess.Popen(app_executable)
                    return f"Opening {app_name}"
                except Exception as e:
                    return f"Sorry, I couldn't open {app_name}. Error: {str(e)}"
        else:
            try:
                subprocess.Popen(app_name)
                return f"Attempting to open {app_name}"
            except Exception as e:
                return f"Sorry, I couldn't open {app_name}. Error: {str(e)}"

    def close_application(self, app_name):
        app_name = app_name.lower()

        if app_name in self.common_apps:
            app_executable = self.common_apps[app_name]
            try:
                subprocess.call(["taskkill", "/F", "/IM", app_executable])
                return f"Closing {app_name}"
            except Exception as e:
                return f"Sorry, I couldn't close {app_name}. Error: {str(e)}"
        else:
            return f"Application {app_name} is not recognized in the common apps list."

    def type_in_application(self, text):
        try:
            pyautogui.typewrite(text)
            return f"Typing '{text}'"
        except Exception as e:
            return f"Failed to type text. Error: {str(e)}"
