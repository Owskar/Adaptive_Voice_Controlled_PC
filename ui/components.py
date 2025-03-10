# ui/components.py
import streamlit as st


def setup_ui(functionalities):
    # Main app description
    st.markdown(
        """
        <div class='intro-text'>
            This application allows you to control your PC and access various services 
            using voice commands. Simply click the 'Start Listening' button and speak 
            your command.
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Sidebar with functionalities
    with st.sidebar:
        st.title("Available Commands")
        st.markdown("### Here's what you can do:")

        for func in functionalities:
            st.markdown(f"- {func}")

        st.markdown(
            """
            ### Example Commands:
            - "Open Chrome"
            - "Search for cats"
            - "What is the weather in London"
            - "Play music"
            - "Take a screenshot"
        """
        )


def show_command_result(result, type="command"):
    """Display command results with appropriate styling"""
    css_class = {
        "command": "command-result",
        "error": "error-text",
        "success": "recognized-text",
        "reminder": "reminder-text",
        "email": "email-sent-text",
        "screenshot": "screenshot-text",
    }.get(type, "command-result")

    st.markdown(f"<div class='{css_class}'>{result}</div>", unsafe_allow_html=True)


def show_listening_indicator():
    """Show an animated listening indicator"""
    with st.spinner("Listening..."):
        st.markdown(
            """
            <div class='listening-text'>
                <span class="dot-1">.</span>
                <span class="dot-2">.</span>
                <span class="dot-3">.</span>
            </div>
        """,
            unsafe_allow_html=True,
        )
