from spotipy import util

print("""
1. Please login into https://developer.spotify.com/dashboard/
2. Click on 'Create and app' and enter the details as desired
3. Once created click on the app name and then click on 'Edit Settings'
4. In the 'Redirect URLs' section enter https://localhost and click on add and scroll to the bottom and click save
5. From the detail page copy the client ID and the client secret.
""")
username = input("Enter the spotify account username: ")
client_id = input("Enter the Client ID obtained from the previous step: ")
client_secret=input("Enter the Client Secret obtained from the previous step: ")
token = util.prompt_for_user_token(username=username,
                                            scope="user-read-playback-state",
                                            client_id=client_id,
                                            client_secret=client_secret,
                                            redirect_uri="http://localhost")
print('Your session string has ben saved as .cache-' + username)
print('Copy the contents of this file to wherever you deploy the bot.\n Note: This file is valid only for 1 hour from the time it is generated')