# services/reminder.py
import time
import streamlit as st
from threading import Timer
from plyer import notification
import re
from datetime import datetime


class ReminderService:
    def __init__(self):
        self.reminders = []
        if "reminder_messages" not in st.session_state:
            st.session_state.reminder_messages = []
        if "reminder_messages" not in st.session_state:
            st.session_state.reminder_messages = []

    def parse_time(self, time_str):
        # Convert time string to seconds
        time_dict = {
            "hr": 3600,
            "hour": 3600,
            "min": 60,
            "minute": 60,
            "sec": 1,
            "second": 1,
        }
        total_seconds = 0

        matches = re.findall(
            r"(\d+)\s*(hr|hour|min|minute|sec|second)s?", time_str.lower()
        )
        for value, unit in matches:
            total_seconds += int(value) * time_dict[unit]

        return total_seconds if total_seconds > 0 else None

    def set_reminder(self, reminder_text, time_str):
        try:
            time_seconds = self.parse_time(time_str)
            if not time_seconds:
                return "Invalid time format. Please specify time in hours, minutes, or seconds."

            # Create reminder timestamp
            reminder_time = datetime.now().strftime("%H:%M:%S")

            # Schedule the reminder
            timer = Timer(
                time_seconds,
                self._reminder_callback,
                args=[reminder_text, reminder_time],
            )
            timer.start()

            # Store reminder info
            self.reminders.append(
                {"text": reminder_text, "timer": timer, "time": reminder_time}
            )

            # Create a human-readable time string
            hours = time_seconds // 3600
            minutes = (time_seconds % 3600) // 60
            seconds = time_seconds % 60
            time_parts = []
            if hours:
                time_parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
            if minutes:
                time_parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
            if seconds:
                time_parts.append(f"{seconds} second{'s' if seconds != 1 else ''}")
            time_str = " and ".join(time_parts)

            return f"Reminder set: {reminder_text} in {time_str}"
        except Exception as e:
            return f"Error setting reminder: {str(e)}"

    def _reminder_callback(self, reminder_text, set_time):
        # Add reminder to session state
        reminder_msg = {
            "text": reminder_text,
            "time": set_time,
            "triggered": datetime.now().strftime("%H:%M:%S"),
        }
        st.session_state.reminder_messages.append(reminder_msg)

        # Display reminder
        st.write(
            f"""<div class='reminder-text'>
                🔔 REMINDER: {reminder_text}<br>
                <small>Set at: {set_time} | Triggered at: {reminder_msg['triggered']}</small>
                </div>""",
            unsafe_allow_html=True,
        )

        # Remove completed reminder from list
        self.reminders = [r for r in self.reminders if r["text"] != reminder_text]
