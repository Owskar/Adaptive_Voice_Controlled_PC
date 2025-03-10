# config/settings.py


class Config:
    # API Keys
    WOLFRAM_APP_ID = "7KVR96-HUHX5VG3JL"
    GENAI_API_KEY = "AIzaSyDOhz3gyd2MR8HoeuHs46dR10DlLiT51xQ"
    WEATHER_API_KEY = "bd5e378503939ddaee76f12ad7a97608"
    NEWS_API_KEY = "de44005bae66482eb56abc8cc5a6ea68"

    # Email Settings
    EMAIL_FROM = "oskarganbawale@gmail.com"
    EMAIL_PASSWORD = "oles obtq rawo mcva"
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587

    # Email Contact List
    EMAIL_CONTACTS = {
        "Ritesh Gurav": "riteshgurav001@gmail.com",
        "samruddhi patil": "samruddhi1406@gmail.com",
        "sanika chavan": "sanikachavan2034@gmail.com",
        "Mansi Jadhav": "manujadhav276@gmail.com",
        "Nikhil": "nikhil.ishware01@gmail.com",
        # Add more contacts as needed
    }

    # File Paths
    MUSIC_DIR = "C:\\Users\\Admin\\Music"

    # Available Functionalities
    FUNCTIONALITIES = [
        "Open Applications",
        "Search the Web",
        "Get Weather Information",
        "Play Music",
        "Stop Music",
        "Check System Status",
        "Set Reminders",
        "Send Email",
        "Get Latest News",
        "Take Screenshot",
    ]
