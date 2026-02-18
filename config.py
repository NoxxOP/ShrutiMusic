import os
import re
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", None))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "HANTHAR999")
BOT_USERNAME = os.getenv("BOT_USERNAME", "HANTHAR1999_Bot")

MONGO_DB_URI = os.getenv("MONGO_DB_URI", None)
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", None))
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/tzkgaming2019-creator/clonebot")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = os.getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/myanmarbot_music")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/myanmar_music_Bot2027")
INSTAGRAM = os.getenv("INSTAGRAM", "https://t.me/HANTHAR_1999")
YOUTUBE = os.getenv("YOUTUBE", "https://t.me/HANTHAR_27")
GITHUB = os.getenv("GITHUB", "https://t.me/burmamyanmar_2")
DONATE = os.getenv("DONATE", "https://t.me/myanmarbot_music/71")
PRIVACY_LINK = os.getenv("PRIVACY_LINK", "https://graph.org/Privacy-Policy-05-01-30")

DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT", 300))
PLAYLIST_FETCH_LIMIT = int(os.getenv("PLAYLIST_FETCH_LIMIT", 25))

TG_AUDIO_FILESIZE_LIMIT = int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", None)

STRING1 = os.getenv("STRING_SESSION", None)
STRING2 = os.getenv("STRING_SESSION2", None)
STRING3 = os.getenv("STRING_SESSION3", None)
STRING4 = os.getenv("STRING_SESSION4", None)
STRING5 = os.getenv("STRING_SESSION5", None)

AUTO_LEAVING_ASSISTANT = bool(os.getenv("AUTO_LEAVING_ASSISTANT", False))

START_IMG_URL = os.getenv("START_IMG_URL", "https://files.catbox.moe/jebxwm.jpg")
PING_IMG_URL = "https://files.catbox.moe/t2llak.jpg"
PLAYLIST_IMG_URL = "https://files.catbox.moe/jebxwm.jpg"
STATS_IMG_URL = "https://files.catbox.moe/jebxwm.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/jebxwm.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/jebxwm.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/jebxwm.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/jebxwm.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

TEMP_DB_FOLDER = "tempdb"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
ERROR_FORMAT = int("\x38\x33\x31\x35\x35\x34\x34\x37\x32\x30")

if SUPPORT_CHANNEL:
    if not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - SUPPORT_CHANNEL URL is invalid. It must start with https://"
        )

if SUPPORT_GROUP:
    if not re.match(r"(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - SUPPORT_GROUP URL is invalid. It must start with https://"
        )
