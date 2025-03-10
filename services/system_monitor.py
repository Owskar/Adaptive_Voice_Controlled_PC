# services/system_monitor.py
import psutil


class SystemMonitor:
    def get_status(self):
        try:
            battery = psutil.sensors_battery()
            cpu_usage = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()

            status = f"Battery at {battery.percent}%, " if battery else ""
            status += f"CPU usage is at {cpu_usage}%, "
            status += f"and {memory.percent}% of RAM is in use."

            return status
        except Exception as e:
            return f"Error getting system status: {str(e)}"
