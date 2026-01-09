

from os import environ

API_ID = int(environ.get("API_ID", "26271673"))
API_HASH = environ.get("API_HASH", "0e807111856890e4770b3e5a3324ec5f")
BOT_TOKEN = environ.get("BOT_TOKEN", "8276591766:AAFDGk1RUJPPLsXs-pxk5aHxreKHYIskS3w")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "TotalFileStore2025_bot")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/TotalFileStore2025_bot")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "COURSEWALLAH2025").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "820017857"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")





