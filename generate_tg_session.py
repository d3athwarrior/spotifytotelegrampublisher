from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""Please go-to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details""")

API_KEY = input("Enter API_KEY obtained from the above process: ")
API_HASH = input("Enter API_HASH obtained from the above process: ")

with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
    print("Here is your userbot string, copy it to a safe place !!")
    print("")
    print(client.session.save())
    print("")
    print("Enjoy your Spotify publisher bot!")