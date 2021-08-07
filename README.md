## TGForwarderClient - bot to forward messages from channels to chats in Telegram.

1. Visit [Telegram Apps API](https://my.telegram.org/apps) and log in with your Telegram Account.
2. Fill out the form to register a new Telegram application.
3. After registration you get and API key. It consists of two parts: `api_id` and `api_hash` - set those as env variables to `$API_ID` and `$API_HASH` (you can save them to `.env` file or directly in docker-compose).
4. Run the app interactively:
```docker run -it -e API_ID -e API_HASH qqalexqq/tgforwarderclient:latest python export_session.py```
5. Input data in interactive window:
```Enter phone number or bot token: aaa
Is "+aaa" correct? (y/N): y
The confirmation code has been sent via Telegram app
Enter confirmation code: bbb
The two-step verification is enabled and a password is required
Password hint: None
Enter password (empty to recover): ccc
---
abcdefghijklmnopqrstuvwxyz (`long string`)
```
6. Copy the last string from the output - the long string. Set it to an env var `$SESSION_KEY`.
7. Set up variables in docker-compose: `BOT_CHANNELS` and `BOT_CHATS`. Examples are provided there.

8. After all things done you can start the container:
```
docker-compose build
docker-compose up -d
```
