import os
import re
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = 37167023
API_HASH = os.getenv("06879a10307f6e6db8114b911295a6ae")
BOT_TOKEN = os.getenv("8511575655:AAFp6vSTokoh5Ou6GVxrd6XH90-C53Gvve4")
OWNER_ID = 8785619142
OWNER_USERNAME = os.getenv("SIKANDER_025")
BOT_USERNAME = os.getenv("AstarrMusicBot")

MONGO_DB_URI = os.getenv("mongodb+srv://bikash:bikash@bikash.3jkvhp7.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = "-1003977469179"
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/sikander025/AstarrMusic1")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = os.getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/AstarrMusicChannel")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/AstarrMusicSupport")
INSTAGRAM = os.getenv("INSTAGRAM", "https://instagram.com/sikander__025")
YOUTUBE = os.getenv("YOUTUBE", "https://youtube.com/@SIKANDER_025")
GITHUB = os.getenv("GITHUB", "https://github.com/NoxxOP")
DONATE = os.getenv("DONATE", "https://t.me/ShrutiBots/91")
PRIVACY_LINK = os.getenv("PRIVACY_LINK", "https://graph.org/Privacy-Policy-05-01-30")

DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT", 300))
PLAYLIST_FETCH_LIMIT = int(os.getenv("PLAYLIST_FETCH_LIMIT", 25))

TG_AUDIO_FILESIZE_LIMIT = int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", None)

STRING1 = "AgI3H68ABpCm_mFRt8VBUQpDIJdL00MEfjf02qU33r0Xzhpv1fjG2kmPF22OV61K_qHK4m15VCCsrjA662SFe9DsoRFRx2b_Mxqd13NlfwS7dUgQhVarGlO-vkCHy0yUTdFYm8D4jGMphvdE3W8Mt-7F2LP7kztuIKVjDRH9Fob8lbKTnnLaZpWhpiG5jM9Rr6Rl1Ss0ZvR_cFjCV30r6pLCBLafVt-7rwQ23JHClgDLp15VM1rY1HzcuguJC6kUj7Dm9fvJ9h8QAEK8q80IrjgqiRz02B8oHw8u-LR2SIOQpk5Oc2SXQ3KOmTTEuJ1CORKl0ySbpS1rTT0P2kvdWVvki81jzAAAAAILqejGAA"
STRING2 = os.getenv("STRING_SESSION2", None)
STRING3 = os.getenv("STRING_SESSION3", None)
STRING4 = os.getenv("STRING_SESSION4", None)
STRING5 = os.getenv("STRING_SESSION5", None)

AUTO_LEAVING_ASSISTANT = bool(os.getenv("AUTO_LEAVING_ASSISTANT", False))

START_IMG_URL = os.getenv("START_IMG_URL", "https://files.catbox.moe/7q8bfg.jpg")
PING_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
PLAYLIST_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
STATS_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/eehxb4.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/eehxb4.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
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
