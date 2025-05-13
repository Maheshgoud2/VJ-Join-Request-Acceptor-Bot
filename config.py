from os import environ

API_ID = int(environ.get("API_ID", "20959976"))
API_HASH = environ.get("API_HASH", "4f648d2c4c0fd1b89a995bb85b2dba67")
BOT_TOKEN = environ.get("BOT_TOKEN", "8069761561:AAH2_2k_rKsKJh8Q9eEmh_AIef-8h8D-66c")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002663107514"))
ADMINS = int(environ.get("ADMINS", "-1008098368518"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://boyboy:boyboy@cluster0.ar8xyfh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', False))
