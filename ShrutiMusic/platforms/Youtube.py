import asyncio
import os
import re
import json
from typing import Union
import requests
import yt_dlp
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message
from youtubesearchpython.__future__ import VideosSearch
from ShrutiMusic.utils.database import is_on_off
from ShrutiMusic import app
from ShrutiMusic.utils.formatters import time_to_seconds
import os
import glob
import random
import logging
import pymongo
from pymongo import MongoClient
import aiohttp
import config
import traceback
from ShrutiMusic import LOGGER

API_URL = None
API_KEY = None

def cookie_txt_file():
    cookie_dir = "ShrutiMusic/cookies"
    if not os.path.exists(cookie_dir):
        return None
    cookies_files = [f for f in os.listdir(cookie_dir) if f.endswith(".txt")]
    if not cookies_files:
        return None
    cookie_file = os.path.join(cookie_dir, random.choice(cookies_files))
    return cookie_file

async def load_api_credentials():
    global API_URL, API_KEY
    logger = LOGGER("ShrutiMusic/platforms/Youtube.py")
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://gist.githubusercontent.com/YaduvanshiNand/a38b3afadc76ee987f7a29617ae6e90c/raw/17e1a32ad03308351cfaffc7988acb943a10e337/api.txt") as response:
                if response.status == 200:
                    content = await response.text()
                    for line in content.strip().split('\n'):
                        if line.startswith('API_URL'):
                            API_URL = line.split('=')[1].strip().strip('"')
                        elif line.startswith('API_KEY'):
                            API_KEY = line.split('=')[1].strip().strip('"')
                    
                    if API_URL and API_KEY:
                        logger.info(f"API credentials loaded successfully")
                    else:
                        logger.error("Failed to parse API credentials")
                else:
                    logger.error(f"Failed to fetch credentials. HTTP Status: {response.status}")
    except Exception as e:
        logger.error(f"Error loading API credentials: {e}")

try:
    loop = asyncio.get_event_loop()
    if loop.is_running():
        asyncio.create_task(load_api_credentials())
    else:
        loop.run_until_complete(load_api_credentials())
except RuntimeError:
    pass

async def download_song(link: str) -> str:
    global API_URL, API_KEY
    
    if not API_URL or not API_KEY:
        await load_api_credentials()
        if not API_URL or not API_KEY:
            logger = LOGGER("ShrutiMusic/platforms/Youtube.py")
            logger.error("API credentials not available")
            return None
    
    video_id = link.split('v=')[-1].split('&')[0] if 'v=' in link else link
    logger = LOGGER("ShrutiMusic/platforms/Youtube.py")
    logger.info(f"🎵 [AUDIO] Starting download process for ID: {video_id}")

    if not video_id or len(video_id) < 3:
        return

    DOWNLOAD_DIR = "downloads"
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    file_path = os.path.join(DOWNLOAD_DIR, f"{video_id}.webm")

    if os.path.exists(file_path):
        logger.info(f"🎵 [LOCAL] Found existing file for ID: {video_id}")
        return file_path

    try:
        async with aiohttp.ClientSession() as session:
            payload = {"url": video_id, "type": "audio"}
            headers = {
                "Content-Type": "application/json",
                "X-API-KEY": API_KEY
            }

            async with session.post(f"{API_URL}/download", json=payload, headers=headers) as response:
                data = await response.json(content_type=None)

                if response.status != 200:
                    logger.error(f"[AUDIO] API returned HTTP {response.status} → {data}")
                    return

                if data.get("status") == "error":
                    detail = data.get("detail", "Unknown error")
                    logger.error(f"[AUDIO] API Error: {detail}")
                    return

                if data.get("status") != "success" or not data.get("download_url"):
                    logger.error(f"[AUDIO] Unexpected API response: {data}")
                    return

                download_link = f"{API_URL}{data['download_url']}"

            async with session.get(download_link) as file_response:
                if file_response.status != 200:
                    logger.error(f"[AUDIO] Download failed ({file_response.status}) for ID: {video_id}")
                    return
                with open(file_path, "wb") as f:
                    async for chunk in file_response.content.iter_chunked(8192):
                        f.write(chunk)

        logger.info(f"🎵 [API] Download completed successfully for ID: {video_id}")
        return file_path

    except Exception as e:
        logger.error(f"[AUDIO] Exception for ID: {video_id} - {e}")
        return

async def download_video(link: str) -> str:
    global API_URL, API_KEY
    
    if not API_URL or not API_KEY:
        await load_api_credentials()
        if not API_URL or not API_KEY:
            logger = LOGGER("ShrutiMusic/platforms/Youtube.py")
            logger.error("API credentials not available")
            return None
    
    video_id = link.split('v=')[-1].split('&')[0] if 'v=' in link else link
    logger = LOGGER("ShrutiMusic/platforms/Youtube.py")
    logger.info(f"🎥 [VIDEO] Starting download process for ID: {video_id}")

    if not video_id or len(video_id) < 3:
        return

    DOWNLOAD_DIR = "downloads"
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    file_path = os.path.join(DOWNLOAD_DIR, f"{video_id}.mkv")

    if os.path.exists(file_path):
        logger.info(f"🎥 [LOCAL] Found existing file for ID: {video_id}")
        return file_path

    try:
        async with aiohttp.ClientSession() as session:
            payload = {"url": video_id, "type": "video"}
            headers = {
                "Content-Type": "application/json",
                "X-API-KEY": API_KEY
            }

            async with session.post(f"{API_URL}/download", json=payload, headers=headers) as response:
                data = await response.json(content_type=None)

                if response.status != 200:
                    logger.error(f"[VIDEO] API returned HTTP {response.status} → {data}")
                    return

                if data.get("status") == "error":
                    detail = data.get("detail", "Unknown error")
                    logger.error(f"[VIDEO] API Error: {detail}")
                    return

                if data.get("status") != "success" or not data.get("download_url"):
                    logger.error(f"[VIDEO] Unexpected API response: {data}")
                    return

                download_link = f"{API_URL}{data['download_url']}"

            async with session.get(download_link) as file_response:
                if file_response.status != 200:
                    logger.error(f"[VIDEO] Download failed ({file_response.status}) for ID: {video_id}")
                    return
                with open(file_path, "wb") as f:
                    async for chunk in file_response.content.iter_chunked(8192):
                        f.write(chunk)

        logger.info(f"🎥 [API] Download completed successfully for ID: {video_id}")
        return file_path

    except Exception as e:
        logger.error(f"[VIDEO] Exception for ID: {video_id} - {e}")
        return

async def check_file_size(link):
    async def get_format_info(link):
        cookie_file = cookie_txt_file()
        if not cookie_file:
            print("No cookies found. Cannot check file size.")
            return None
            
        proc = await asyncio.create_subprocess_exec(
            "yt-dlp",
            "--cookies", cookie_file,
            "-J",
            link,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        if proc.returncode != 0:
            print(f'Error:\n{stderr.decode()}')
            return None
        return json.loads(stdout.decode())

    def parse_size(formats):
        total_size = 0
        for format in formats:
            if 'filesize' in format:
                total_size += format['filesize']
        return total_size

    info = await get_format_info(link)
    if info is None:
        return None
    
    formats = info.get('formats', [])
    if not formats:
        print("No formats found.")
        return None
    
    total_size = parse_size(formats)
    return total_size

async def shell_cmd(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    out, errorz = await proc.communicate()
    if errorz:
        if "unavailable videos are hidden" in (errorz.decode("utf-8")).lower():
            return out.decode("utf-8")
        else:
            return errorz.decode("utf-8")
    return out.decode("utf-8")


class YouTubeAPI:
    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="
        self.regex = r"(?:youtube\.com|youtu\.be)"
        self.status = "https://www.youtube.com/oembed?url="
        self.listbase = "https://youtube.com/playlist?list="
        self.reg = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    async def exists(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        return bool(re.search(self.regex, link))

    async def url(self, message_1: Message) -> Union[str, None]:
        messages = [message_1]
        if message_1.reply_to_message:
            messages.append(message_1.reply_to_message)
        for message in messages:
            if message.entities:
                for entity in message.entities:
                    if entity.type == MessageEntityType.URL:
                        text = message.text or message.caption
                        return text[entity.offset: entity.offset + entity.length]
            elif message.caption_entities:
                for entity in message.caption_entities:
                    if entity.type == MessageEntityType.TEXT_LINK:
                        return entity.url
        return None

    async def details(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            title = result["title"]
            duration_min = result["duration"]
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            vidid = result["id"]
            duration_sec = int(time_to_seconds(duration_min)) if duration_min else 0
        return title, duration_min, duration_sec, thumbnail, vidid

    async def title(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            return result["title"]

    async def duration(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            return result["duration"]

    async def thumbnail(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            return result["thumbnails"][0]["url"].split("?")[0]

    async def video(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        try:
            downloaded_file = await download_video(link)
            if downloaded_file:
                return 1, downloaded_file
            else:
                return 0, "Video API did not return a valid file."
        except Exception as e:
            print(f"Video API failed: {e}")
            return 0, f"Video API failed: {e}"

    async def playlist(self, link, limit, user_id, videoid: Union[bool, str] = None):
        if videoid:
            link = self.listbase + link
        if "&" in link:
            link = link.split("&")[0]
        cookie_file = cookie_txt_file()
        if not cookie_file:
            return []
        playlist = await shell_cmd(
            f"yt-dlp -i --get-id --flat-playlist --cookies {cookie_file} --playlist-end {limit} --skip-download {link}"
        )
        try:
            result = [key for key in playlist.split("\n") if key]
        except:
            result = []
        return result

    async def track(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        results = VideosSearch(link, limit=1)
        for result in (await results.next())["result"]:
            title = result["title"]
            duration_min = result["duration"]
            vidid = result["id"]
            yturl = result["link"]
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        track_details = {
            "title": title,
            "link": yturl,
            "vidid": vidid,
            "duration_min": duration_min,
            "thumb": thumbnail,
        }
        return track_details, vidid

    async def formats(self, link: str, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        cookie_file = cookie_txt_file()
        if not cookie_file:
            return [], link
        ytdl_opts = {"quiet": True, "cookiefile": cookie_file}
        ydl = yt_dlp.YoutubeDL(ytdl_opts)
        with ydl:
            formats_available = []
            r = ydl.extract_info(link, download=False)
            for format in r["formats"]:
                try:
                    if "dash" not in str(format["format"]).lower():
                        formats_available.append(
                            {
                                "format": format["format"],
                                "filesize": format.get("filesize"),
                                "format_id": format["format_id"],
                                "ext": format["ext"],
                                "format_note": format["format_note"],
                                "yturl": link,
                            }
                        )
                except:
                    continue
        return formats_available, link

    async def slider(self, link: str, query_type: int, videoid: Union[bool, str] = None):
        if videoid:
            link = self.base + link
        if "&" in link:
            link = link.split("&")[0]
        a = VideosSearch(link, limit=10)
        result = (await a.next()).get("result")
        title = result[query_type]["title"]
        duration_min = result[query_type]["duration"]
        vidid = result[query_type]["id"]
        thumbnail = result[query_type]["thumbnails"][0]["url"].split("?")[0]
        return title, duration_min, thumbnail, vidid

    async def download(
        self,
        link: str,
        mystic,
        video: Union[bool, str] = None,
        videoid: Union[bool, str] = None,
        songaudio: Union[bool, str] = None,
        songvideo: Union[bool, str] = None,
        format_id: Union[bool, str] = None,
        title: Union[bool, str] = None,
    ) -> str:
        if videoid:
            link = self.base + link

        try:
            if songvideo or songaudio:
                downloaded_file = await download_song(link)
                if downloaded_file:
                    return downloaded_file, True
                else:
                    return None, False
            elif video:
                downloaded_file = await download_video(link)
                if downloaded_file:
                    return downloaded_file, True
                else:
                    return None, False
            else:
                downloaded_file = await download_song(link)
                if downloaded_file:
                    return downloaded_file, True
                else:
                    return None, False
        except Exception as e:
            print(f"API download failed: {e}")
            return None, False
