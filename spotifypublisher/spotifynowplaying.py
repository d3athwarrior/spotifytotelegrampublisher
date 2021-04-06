# from userbot.modules.sql_helper.spotifypublished import is_song_published, publish_song
from datetime import date, datetime
import os

import requests
from sqlalchemy.sql.functions import now
from database.spotifypublished import SpotifyPlayed, is_song_published, publish_song
from spotipy import Spotify, util
from spotifypublisher import BOT, LOGS, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_LIST_CHAT_ID, SPOTIFY_PLAY_TIME_BEFORE_PUBLISH, SPOTIFY_QUERY_DELAY, SPOTIFY_TIME_BEFORE_REPUBLISH_SECONDS, SPOTIFY_USERNAME
from spotipy.exceptions import SpotifyException
from telethon.client.telegramclient import TelegramClient
from telethon.sessions.string import StringSession
from apscheduler.schedulers.asyncio import AsyncIOScheduler

spotify_client = None
song_publish_grace_detail: dict = dict()

def authenticateSpotify():
    global spotify_client
    try:
        token = util.prompt_for_user_token(username=SPOTIFY_USERNAME,
                                        scope="user-read-playback-state",
                                        client_id=SPOTIFY_CLIENT_ID,
                                        client_secret=SPOTIFY_CLIENT_SECRET,
                                        redirect_uri="http://localhost")
    except SpotifyException as ex:
        LOGS.error('Spotify error:' + ex.msg)

    spotify_client = Spotify(auth=token)

async def queryNowPlaying():
    global spotify_client
    global song_publish_grace_detail
    album: str = None
    song: str = None
    artist: str = None
    album_art_URL: str = None,
    song_detail: SpotifyPlayed = None
    publish_grace_time_elapsed: float = None

    try:
        results = None
        if spotify_client == None:
            authenticateSpotify()
        results = spotify_client.current_playback()
    except SpotifyException as ex:
        LOGS.error("Spotify Error: " + ex.msg)
        authenticateSpotify()
        results = spotify_client.current_playback()
    if (results != None):
        song = str(results['item']['name'])
        album = str(results['item']['album']['name'])

        for artistDetail in results['item']['artists']:
            if artist != None:
                artist += ',' + str(artistDetail['name'])
            else:
                artist = str(artistDetail['name'])

        for album_art_detail in results['item']['album']['images']:
            if int(album_art_detail['height']) <= 300 and int(album_art_detail['height']) > 200:
                album_art_URL = album_art_detail['url']

        song_detail = is_song_published(song, album, artist)
        if (not song+album+artist in song_publish_grace_detail.keys()):
            song_publish_grace_detail[song+album+artist] = datetime.now()
        
        publish_grace_time_elapsed = (datetime.now() - song_publish_grace_detail[song+album+artist]).total_seconds()

        if ((song_detail == None) and publish_grace_time_elapsed > SPOTIFY_PLAY_TIME_BEFORE_PUBLISH):
            # Republish after grace time is still broken. Due to the nature of SQL and the threads being executed concurrently, the songs are being published
            # twice. This is an issue.
            # if ((song_detail == None or __republish_grace_time_elapsed(song_detail)) and publish_grace_time_elapsed > SPOTIFY_PLAY_TIME_BEFORE_PUBLISH):
            message_body = '<strong>Song     : </strong>' + song + '\n<strong>Album  : </strong>' + album + '\n<strong>Artist    : </strong>' + artist
            browser_link = str(results['item']['album']['external_urls']['spotify']) + '?highlight=' + str(results['item']['uri'])
            mobile_link = str(results['item']['external_urls']['spotify'])
            LOGS.info("Publishing: " + message_body)
            if (song_detail == None):
                publish_song(name=song, album=album, artist=artist)
            else:
                publish_song(song_detail=song_detail)
            open('image.png', 'wb').write(requests.get(url=album_art_URL).content)
            await BOT.send_file(SPOTIFY_LIST_CHAT_ID, file = 'image.png', caption=message_body +
                                        '\n\n<a href="' + browser_link + '">Open Browser Link</a>' +
                                        '\n<a href="' + mobile_link + '">Open Mobile Link</a>', parse_mode='html')
            
            song_publish_grace_detail.pop(song+album+artist)
            
            os.remove('image.png')

def __republish_grace_time_elapsed(song_details: SpotifyPlayed) -> bool:
    """
        Function to check if a song has been played for the configured time
    """
    return (datetime.now() - song_details.last_played).total_seconds() > SPOTIFY_TIME_BEFORE_REPUBLISH_SECONDS

scheduler = AsyncIOScheduler()
scheduler.add_job(queryNowPlaying, 'interval', seconds=SPOTIFY_QUERY_DELAY, misfire_grace_time=4, coalesce=True)
scheduler.start()