# ui/styles.py
import streamlit as st


def apply_styles():
    st.markdown(
        """
        <style>
        .listening-text {
            font-size: 20px;
            color: #ffcc00;
            animation: fadeIn 2s;
        }

        .recognized-text {
            font-size: 18px;
            color: #00cc00;
            animation: fadeIn 2s;
        }

        .error-text {
            font-size: 18px;
            color: #ff0000;
            animation: fadeIn 2s;
        }

        .reminder-text {
            font-size: 18px;
            color: #0099ff;
            animation: fadeIn 2s;
            padding: 10px;
            border-left: 4px solid #0099ff;
            background-color: #f0f8ff;
            margin: 10px 0;
        }
        
        .reminder-alert {
            font-size: 18px;
            color: #ff3300;
            animation: fadeIn 2s;
            padding: 15px;
            border-radius: 5px;
            background-color: #fff3f3;
            border: 2px solid #ff3300;
            margin: 10px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .email-sent-text {
            font-size: 18px;
            color: #009900;
            animation: fadeIn 2s;
        }

        .screenshot-text {
            font-size: 18px;
            color: #ff9900;
            animation: fadeIn 2s;
        }

        .command-result {
            font-size: 18px;
            color: #333333;
            animation: slideIn 2s;
        }

        .goodbye-text {
            font-size: 20px;
            color: #ff6600;
            animation: fadeOut 2s;
        }

        .stButton > button {
            width: 100%;
            padding: 10px 20px;
            font-size: 18px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: transform 0.2s;
        }

        .stButton > button:hover {
            transform: scale(1.02);
        }

        .stButton > button:active {
            transform: scale(0.98);
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        @keyframes fadeOut {
            from { opacity: 1; }
            to { opacity: 0; }
        }

        @keyframes slideIn {
            from { transform: translateX(-100%); }
            to { transform: translateX(0); }
        }

        .sidebar .sidebar-content {
            background-color: #f8f9fa;
        }

        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        </style>
    """,
        unsafe_allow_html=True,
    )