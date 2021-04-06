from logging import DEBUG, INFO, basicConfig, getLogger
import os
from dotenv import load_dotenv
from distutils.util import strtobool as sb

from telethon.client.telegramclient import TelegramClient
from telethon.sessions.string import StringSession


load_dotenv('config.env')

CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                level=INFO)
LOGS = getLogger(__name__)

# Telegram App KEY and HASH
API_KEY = os.environ.get("API_KEY", None)
API_HASH = os.environ.get("API_HASH", None)

# Session String
STRING_SESSION = os.environ.get("STRING_SESSION", None)

# SQL Database URI
DB_URI = os.environ.get("DATABASE_URL", None)

# The Spotify account username to use with spotify now playing publisher publisher
SPOTIFY_USERNAME=os.environ.get('SPOTIFY_USERNAME', '')

# The Spotify client id obtained from the developer dashboard
SPOTIFY_CLIENT_ID=os.environ.get('SPOTIFY_CLIENT_ID', '')

# The Spotify client secret obtained from the developer dashboard
SPOTIFY_CLIENT_SECRET=os.environ.get('SPOTIFY_CLIENT_SECRET', '')

# The user/channel/group (where you are a member) id where the songs need to be published
SPOTIFY_LIST_CHAT_ID=os.environ.get('SPOTIFY_LIST_CHAT_ID', '')

# The delay (in seconds) with which the spotify api should be queried
SPOTIFY_QUERY_DELAY=int(os.environ.get('SPOTIFY_QUERY_DELAY', ''))

# The time (in seconds) to let a song play before publishing it
SPOTIFY_PLAY_TIME_BEFORE_PUBLISH=int(os.environ.get('SPOTIFY_PLAY_TIME_BEFORE_PUBLISH', 45))

# The % of the song to be played before publishing it. Default is 25%.
# SPOTIFY_PLAY_TIME_PERCENT_BEFORE_PUBLISH=float(os.environ.get('SPOTIFY_PLAY_TIME_PERCENT_BEFORE_PUBLISH', 25))

# The time (in hours) to let a song play before publishing it. Default is 120 hours
SPOTIFY_TIME_BEFORE_REPUBLISH_SECONDS=int(os.environ.get('SPOTIFY_TIME_BEFORE_REPUBLISH', 120)) * 60 * 60

BOT = None
if (STRING_SESSION not in ('', None) and API_KEY not in ('', None) and API_HASH not in ('', None) 
    and SPOTIFY_USERNAME not in (None, "") and SPOTIFY_CLIENT_ID not in (None, "")
    and SPOTIFY_CLIENT_SECRET not in (None, "") and SPOTIFY_LIST_CHAT_ID not in (None, "")):
    BOT = TelegramClient(session=StringSession(STRING_SESSION),
                                                api_id=API_KEY,
                                                api_hash=API_HASH)
else:
    raise Exception('Please fill in the correct details in the config')