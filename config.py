import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "8867231877:AAH6T6SKHNo7fTpACCyfWlr4RrLTBv1ai5E")
TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID", "-1003903485012")  # Username каналу

# Tronscan API Configuration
TRONSCAN_API_TOKEN = os.getenv("TRONSCAN_API_TOKEN", "3bfa787b-22a1-4c79-a2f5-b46dc062ee9f")
TRON_ADDRESS = os.getenv("TRON_ADDRESS", "TKvPkbRhRC1XK5sk4P8wShrkuQcYotrH1d")

# Monitoring Configuration
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", "30"))  # секунди між перевірками

