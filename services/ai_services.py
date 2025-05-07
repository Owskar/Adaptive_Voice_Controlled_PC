# services/ai_services.py
import google.generativeai as genai
import streamlit as st


class AIServices:
    def __init__(self):
        # Replace with your API key from Google AI Studio
        self.api_key = "AIzaSyDOhz3gyd2MR8HoeuHs46dR10DlLiT51xQ"
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    def generate_gemini_content(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            result = response.text
            st.write(
                f"<div class='command-result'>{result}</div>", unsafe_allow_html=True
            )
            return result
        except Exception as e:
            error_msg = f"Sorry, I couldn't generate content. Error: {str(e)}"
            st.error(error_msg)
            return error_msg
