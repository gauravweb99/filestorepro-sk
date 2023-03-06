
import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
load_dotenv()


#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28768879"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "3a09b10d2288842e795fb04df10d778c")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001854029035"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1230839024"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://manju:1234@cluster0.s6qpf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot256")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001862840418"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "👋 Hello {first}\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5863383503").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "👋 Hello {first}\n<b>😓 You need to join in my Channel/Group to use me\n😋 Kindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = ""

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)


MULITPLE_BOT_TOKENS = list(os.environ.get("MULITPLE_BOT_TOKENS", "5854093607:AAHZ-xtK3DHDXieT0luR7P0LViiOoyOf-ig 5913605784:AAGX0ZiIIjgqtX8FEwQO9rLiamFikm9QNf8 5033553892:AAF0IDMaCJUxGwqN_RCRqMY8mYPS8QK0PZY 5825503942:AAEKkAKE5BrBI4DIYRa_OsG3jqGovCSb7R4 5718843227:AAGaVjSBFObDNmp7rZyJPLyK7CkUcLug0uE 5500281723:AAES-ntPU_SwyeI2M1D1kU1zIYluCiEdFEI 5777838885:AAELOX6UCciy3I7VD4Rj2R9a-rmnsX5Uwfs 5832973945:AAExPH54u1CsqCNXtOi4VbKtjPFhrYP-_Ls").split())

MULTIPLE_BOT_MODE = len(MULITPLE_BOT_TOKENS) > 1

MULITPLE_BOT_TOKENS.append(TG_BOT_TOKEN)