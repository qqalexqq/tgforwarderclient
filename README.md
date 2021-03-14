## TGForwarderClient - bot to forwards messages from channels to chats.

1. Visit [Telegram Apps API](https://my.telegram.org/apps) and log in with your Telegram Account.
2. Fill out the form to register a new Telegram application.
3. The API key consists of two parts: `api_id` and `api_hash` - set them as env variables to `$API_ID` and `$API_HASH` through `.env` file or whatever you prefer. Also remember to set the name of session through `$SESSION_NAME` - any name is fine.
4. Run the app interactively:
```docker run -it -v $PWD/plugins/:/plugins/ -v $PWD/sessions:/sessions --env-file .env qqalexqq/tgforwarder:latest```
5. Input data in interactive window:
```Enter phone number or bot token: aaa
Is "+aaa" correct? (y/N): y
The confirmation code has been sent via Telegram app
Enter confirmation code: bbb
The two-step verification is enabled and a password is required
Password hint: None
Enter password (empty to recover): ccc
```
6. On complete container will fail - this is normal due to unset variables. Now set up those variables: `CHANNELS=channel,names,through,commas` and `CHAT_IDS=chat,ids,through,commas`. Example:
```CHAT_IDS=-1001005702961
CHANNELS=addmeto,techsparks
```

7. After variables set up you can start the container:
```
docker-compose build
docker-compose up -d
```

#### Possible to use with Bot API (without regular Telegram account)?

Yes, if you add your bot to the channel's admins - otherwise bot can't read channel's messages. It was previously possible with bot api's "forwardMessage" but telegram's authors fixed it and now bot can't access channel's before it was added as an admin of channel.
In that case you will need to change docker image - main.py: replace `app = ...",` with `app = Client('forwarder_bot', 'YOUR_BOT_TOKEN')`
