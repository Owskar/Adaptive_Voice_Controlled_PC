# services/screenshot.py
import pyautogui
import datetime
import os
import streamlit as st


class ScreenshotService:
    def __init__(self):
        # Create a screenshots directory if it doesn't exist
        self.screenshot_dir = "screenshots"
        os.makedirs(self.screenshot_dir, exist_ok=True)

    def take_screenshot(self):
        try:
            # Create timestamp for unique filename
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(self.screenshot_dir, f"screenshot_{timestamp}.png")

            # Take screenshot
            screenshot = pyautogui.screenshot()
            screenshot.save(filename)

            # Display success message
            success_msg = f"Screenshot saved as {filename}"
            st.write(
                f"<div class='screenshot-text'>{success_msg}</div>",
                unsafe_allow_html=True,
            )

            # Display the screenshot in the Streamlit app
            st.image(filename, caption="Screenshot taken", use_column_width=True)

            return success_msg
        except Exception as e:
            error_msg = f"Error taking screenshot: {str(e)}"
            st.error(error_msg)
            return error_msg
