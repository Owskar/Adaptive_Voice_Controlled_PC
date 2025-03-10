import speech_recognition as sr
import pyttsx3
import streamlit as st
from utils.logger import logger
from threading import Lock
import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"


class AudioService:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(AudioService, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "initialized"):
            self.recognizer = sr.Recognizer()
            self.initialized = True
            self.engine = None

    def get_engine(self):
        """Get a fresh engine instance for each speech request"""
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.setProperty("volume", 1.0)
        voices = engine.getProperty("voices")
        if voices:
            engine.setProperty("voice", voices[0].id)
        return engine

    def speak(self, text):
        """Speak text using a new engine instance"""
        if not text:
            return

        try:
            # Create a new engine instance for each speech request
            engine = self.get_engine()
            engine.say(text)
            engine.runAndWait()
            engine.stop()
            # Explicitly delete the engine instance
            del engine

        except Exception as e:
            error_msg = f"Speech error: {str(e)}"
            logger.error(error_msg)
            st.error(error_msg)

    def get_audio(self):
        """Get audio input from microphone"""
        try:
            with sr.Microphone() as source:
                # Visual feedback
                placeholder = st.empty()
                placeholder.info("Listening...")

                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=1)

                # Listen for audio
                audio = self.recognizer.listen(source)

                # Update status
                placeholder.info("Processing...")

                try:
                    # Convert speech to text
                    text = self.recognizer.recognize_google(audio)
                    placeholder.success(f"You said: {text}")
                    logger.info(f"Recognized speech: {text}")
                    return text.lower()
                except sr.UnknownValueError:
                    logger.warning("Could not understand audio")
                    placeholder.error("Could not understand audio")
                    return ""
                except sr.RequestError as e:
                    error_msg = f"Could not request results: {str(e)}"
                    logger.error(error_msg)
                    placeholder.error(error_msg)
                    return ""

        except Exception as e:
            error_msg = f"Error capturing audio: {str(e)}"
            logger.error(error_msg)
            st.error(error_msg)
            return ""


# Initialize singleton instance in Streamlit session state
def get_audio_service():
    if "audio_service" not in st.session_state:
        st.session_state.audio_service = AudioService()
    return st.session_state.audio_service