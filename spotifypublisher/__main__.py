from telethon.client.telegramclient import TelegramClient
from telethon.sessions.string import StringSession
from spotifypublisher.spotifynowplaying import queryNowPlaying
from spotifypublisher import BOT, SPOTIFY_QUERY_DELAY, SPOTIFY_USERNAME, STRING_SESSION
from apscheduler.schedulers.asyncio import AsyncIOScheduler

BOT.start()
scheduler = AsyncIOScheduler()
scheduler.add_job(queryNowPlaying, 'interval', seconds=SPOTIFY_QUERY_DELAY, misfire_grace_time=4, coalesce=True)
scheduler.start()

BOT.run_until_disconnected()