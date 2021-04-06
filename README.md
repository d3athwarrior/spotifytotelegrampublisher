# Spotify to Telegram Publisher

## Overview

A simple python application to publish songs the one has listened to on Spotify to a telegram user/channel/group.
Made using [Telethon](https://github.com/LonamiWebs/Telethon), [Spotipy](https://github.com/plamere/spotipy) and [apscheduler](https://github.com/agronholm/apscheduler)  

This can be customized and integrated into a telegram userbot(use userbots at your own risk) example is available [here](https://github.com/d3athwarrior/userbot).

Example of how posts will look like can be seen [here](https://t.me/d3athwarriorsmusic)

## Features

### Implemented

1. Publish the recently played song only once to a channel/group/personal chat of your choice

### Planned

1. Allow for republishing after 'x' number of days which will be configurable  
2. Provide a configurable option to publish a song only when a user has listened to it for more than the configured time. (The logic here is that for someone to really decide whether they like a song or not it takes at least a few seconds 10, 15 or even more and in this time some may not prefer to really publish this song)  

### Open verification points

1. There is a chance that spotify may rate limit an account for sending in many requests which is yet to be tested

If you want a specific feature or have any suggestion then please raise it [here](https://github.com/d3athwarrior/spotifytotelegrampublisher/issues) or get in touch with me on telegram [@d3athwarrior](https://t.me/d3athwarrior)

## How to use

- **Ensure that you have python3, pip, setuptools installed**

1. Clone the repository
2. Obtain a telegram API key and API hash from <https://my.telegram.org>
3. Run the ```generate_tg_session.py``` file to generate the session string to be used in the application by entering the following command in the terminal while you are in the directory where the repository is cloned:  ```python3 generate_tg_session.py```
4. Run the ```generate_spotify_session.py``` file to generate the Spotify session file which will be used by this application later to communicate with Spotify by entering the following command in the terminal while you are in the directory where the repository is cloned: ```python3 generate_spotify_session.py``` and follow the instructions printed in the console
5. Once done, simply run the following command in the console which is open in the application's directory: ```python3 -m venv virtualenv``` 
6. Run the following command in the same console window: ```source ./virtualenv/bin/activate```
7. Run the following command in the same console window: ```pip install -r requirements.txt```
8. Copy the ```sample_config.env``` file to ```config.env``` and fill in all the fields in the config file as per the description
9. Run the following command in the same console window: ```python -m spotifypublisher```

# Credits

* [Pranav](https://github.com/deltaonealpha) & [Jeel](http://github.com/jeelPatel231) for the idea of using apscheduler
* My friends for the motivation and help in designing the output of the application
