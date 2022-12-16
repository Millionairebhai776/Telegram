import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID", "1377849")
    API_HASH = getenv("API_HASH", "2aba0868b0b9da9c4dd9ad656487078c")
    TOKEN = getenv("TOKEN", "5892062017:AAGF4SqtYrU38VjlDoOc-NSblqABRH74Hok")
    OWNER_ID = getenv("OWNER_ID", 611969501)
    STRING_SESSION = getenv("STRING_SESSION", "1BVtsOJ0Buzp5hmNxZ86gBwwOCZYM8I7I2CeVE0JrdNPROj9ABEK-KDyoJv8IYDR0_YcVh3IpqMBmo69Qq3vfaT5fRPXAB0mwQk27vBSYH9b0Oe6sSke2A0bJ-DU5nh4UxoYZwTVXViAk1qR4GlCQ9duG8II2qhzn_bZtPzoF_Bca0OMOeh9t7XCWgA00blSSNGZ8lSAlvMMUWJ-_xss4c_0QAfjsNWgwlL1dXmmIoQQsg1n42FPuxI5CunSGbl9ZCzLJ3aX9jAjXEtiYee2kTmizqJ0hHsMbBIX_hi0oiVmXQ6RciSjr27c4aYPFqVz0es-9vwu78OlYtZkvWxpQax8xbZY7SBY=")
    OWNER_USERNAME = getenv("OWNER_USERNAME", "@FILMWORLDOFFICIA")
    DB_URI = getenv("DATABASE_URL", "")
    DB_URI = DB_URI.replace("postgres", "postgresql")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "-1001284286847")
    GBAN_LOGS = getenv("GBAN_LOGS", "-1001284286847")
    SYS_ADMIN = getenv("SYS_ADMIN", "611969501")
    DEV_USERS = getenv("DEV_USERS", "611969501")
    LOAD = getenv("LOAD")
    WEBHOOK = False
    SPB_MODE = True
    DROP_UPDATES = False
    DEBUG = False
    URL = None
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    BAN_STICKER = getenv("BAN_STICKER", "")
    ALLOW_EXCL = True
    CUSTOM_CMD = False
    CASH_API_KEY = getenv("CASH_API_KEY", "https://www.alphavantage.co/support/#api-key")
    TIME_API_KEY = getenv("TIME_API_KEY", "https://timezonedb.com/api")
    WALL_API = getenv("WALL_API", "https://wall.alphacoders.com/api.php")
    spamwatch_api = getenv("spamwatch_api", "https://t.me/SpamWatchBot")
    SPAMMERS = getenv("SPAMMERS", "")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "https://www.last.fm/api/account/create")
    CF_API_KEY = getenv("CF_API_KEY", "coffehouse.intellivoid.net")
    BOT_API_URL = getenv("BOT_API_URL", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("BOT_API_FILE_URL", "https://api.telegram.org/file/bot")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
    ZAID_USER = list(map(int, getenv("DEV_USERS", "1669178360").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))
