from telethon.client.telegramclient import TelegramClient
from telethon.sessions.string import StringSession
from spotifypublisher.spotify_now_playing import query_now_playing
from spotifypublisher import BOT, SPOTIFY_QUERY_DELAY, SPOTIFY_USERNAME, STRING_SESSION
from apscheduler.schedulers.asyncio import AsyncIOScheduler

BOT.start()
scheduler = AsyncIOScheduler()
scheduler.add_job(query_now_playing, 'interval', seconds=SPOTIFY_QUERY_DELAY, misfire_grace_time=4, coalesce=True)
scheduler.start()

BOT.run_until_disconnected()