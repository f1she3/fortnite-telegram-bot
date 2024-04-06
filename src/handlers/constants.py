"""
    This module exposes env constants to the rest of the project.
"""
import os
from dotenv import load_dotenv

# loads variables from .env file into the script's environment
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GROUP_CHAT_ID = os.getenv("GROUP_CHAT_ID")
FORTNITE_API_KEY = os.getenv("FORTNITE_API_KEY")
NEWS_LANG = os.getenv("NEWS_LANG")
DB_NAME = os.getenv("DB_NAME")
DB_PATH = os.getenv("DB_PATH")
