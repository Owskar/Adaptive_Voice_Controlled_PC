# main.py

import streamlit as st
from utils.logger import logger
from core.assistant import Assistant
from ui.styles import apply_styles
from ui.components import setup_ui
from config.settings import Config


def main():
    st.title("Adaptive Voice-Controlled PC Assistant")

    # Apply styles
    apply_styles()

    # Setup UI components
    setup_ui(Config.FUNCTIONALITIES)

    # Initialize assistant
    assistant = Assistant()

    # Start Listening Button
    if st.button("Start Listening"):
        running = True
        while running:
            command = assistant.audio.get_audio()
            running = assistant.execute_command(command)


if __name__ == "__main__":
    main()