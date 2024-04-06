"""
    This module exposes env constants to the rest of the project.
"""
import os
from dotenv import load_dotenv

# loads variables from .env file into the script's environment
load_dotenv()

TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
TG_CHAT_ID = os.getenv("TG_CHAT_ID")
FORTNITE_API_KEY = os.getenv("FORTNITE_API_KEY")
NEWS_LANG = os.getenv("NEWS_LANG")
DB_NAME = os.getenv("DB_NAME")
DB_PATH = os.getenv("DB_PATH")
DB_ABS_PATH=os.path.join(
    os.path.dirname(
        os.path.abspath(__file__)
    ),
    "..",
    "db",
    DB_PATH
)
