1. Visit https://my.telegram.org/apps and log in with your Telegram Account.
2. Fill out the form to register a new Telegram application.
3. Done! The API key consists of two parts: api_id and api_hash.
4. Edit config.ini inside forwader folder with following:
api_id = (your app_id without quotes here)
api_hash = (your app_hash without quotes here)

5. Run the app interactively to authenticate it first:
'docker-compose build'
'docker run -v "$PWD/forwarder:/app" -it qqalexqq/tgforwarder'
Fill in necessary data (phone number + code + two-factor password if needed).
After "INFO: Synced "forwarder_account" in" stop the program execution - Ctrl+C
Beware! Your *.session and config.ini files are personal and must be kept secret.

6. docker-compose build
docker-compose up -d


Possible to use with Bot API (without regular Telegram account)?

Yes, if you add your bot to the channel's admins - otherwise bot can't read channel's messages. It was previously possible with bot api's "forwardMessage" but telegram's authors fixed it and now bot can't access channel before it was added to it as an admin.
In that case the only line you need to change is '''app = Client('forwarder_account')''' to '''app = Client('forwarder_bot', 'YOUR_BOT_TOKEN')''', and comment out lines '''with app:
    for channel in CHANNELS_LIST:
        app.join_chat(channel)'''
everything else works as it was.

7. crontab:

* 1 * * * docker restart tgforwarderclient_forwarder_1
