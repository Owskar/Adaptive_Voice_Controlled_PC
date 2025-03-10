# core/assistant.py

import streamlit as st
from utils.logger import logger
from services.audio import AudioService
from services.applications import ApplicationService
from services.browser import BrowserService
from services.email_service import EmailService
from services.media_player import MediaPlayer
from services.news_service import NewsService
from services.reminder import ReminderService
from services.screenshot import ScreenshotService
from services.system_monitor import SystemMonitor
from services.weather import WeatherService
from services.ai_services import AIServices


class Assistant:
    def __init__(self):
        self.audio = AudioService()
        self.apps = ApplicationService()
        self.browser = BrowserService()
        self.email = EmailService()
        self.media = MediaPlayer()
        self.news = NewsService()
        self.reminder = ReminderService()
        self.screenshot = ScreenshotService()
        self.system = SystemMonitor()
        self.weather = WeatherService()
        self.ai = AIServices()

    def execute_command(self, command):
        if not command:  # Handle empty command
            logger.info("Empty command received")
            return True

        logger.info(f"Executing command: {command}")

        response = None

        try:
            if "open" in command:
                response = self.apps.open_application(command.split("open")[-1].strip())

            elif "close" in command:
                response = self.apps.close_application(
                    command.split("close")[-1].strip()
                )

            elif "search" in command:
                response = self.browser.search(command.split("search")[-1].strip())

            elif "weather in" in command:
                city = command.split("weather in")[-1].strip()
                response = self.weather.get_weather(city)

            elif "play music" in command:
                response = self.media.play_music()

            elif "stop music" in command:
                response = self.media.stop_music()

            elif "system status" in command:
                response = self.system.get_status()

            elif "remind me to" in command:
                reminder = command.split("remind me to")[-1].strip()
                response = self.reminder.set_reminder(reminder, 10)

            elif "send email to" in command:
                # Extract recipient name
                parts = command.split("send email to", 1)[1].strip()

                # Default subject and body if not specified
                subject = "Message from Voice Assistant"
                body = "This is an automated email sent from your voice assistant."

                # Check if there's additional content after the name
                if " saying " in parts:
                    recipient_name, body = parts.split(" saying ", 1)
                    recipient_name = recipient_name.strip()
                else:
                    recipient_name = parts.strip()

                response = self.email.send_email(recipient_name, subject, body)

            elif "news" in command:
                response = self.news.get_latest_news()

            elif "screenshot" in command:
                response = self.screenshot.take_screenshot()

            elif "exit" in command or "quit" in command:
                response = "Goodbye!"
                self.audio.speak(response)
                return False

            elif "type" in command:
                text_to_type = command.split("type")[-1].strip()
                response = self.apps.type_in_application(text_to_type)

            else:
                # Use AI service for unrecognized commands
                response = self.ai.generate_gemini_content(command)

            # Speak the response if it's not None
            if response:
                self.audio.speak(response)

        except Exception as e:
            error_msg = f"Error executing command: {str(e)}"
            logger.error(error_msg)
            st.error(error_msg)
            self.audio.speak("Sorry, there was an error executing your command")

        return True