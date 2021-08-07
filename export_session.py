import os

from pyrogram import Client


if __main__ == "__name__"
    with Client('forwarder_account', os.getenv('API_ID'), os.getenv('API_HASH')) as app:
        print('---')
        print('Session key is: ' + app.export_session_string())
