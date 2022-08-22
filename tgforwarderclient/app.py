from functools import partial

from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from tgforwarderclient.handler import channel_handler


def make_app(
    session_name: str,
    api_id: int,
    api_hash: str,
    session_key: str,
    channels: list[str],
    chats: list[int],
) -> Client:
    app = Client(session_name, api_id, api_hash, session_string=session_key)
    handler_callback = partial(channel_handler, channels=channels, chats=chats)
    app.add_handler(MessageHandler(callback=handler_callback, filters=filters.channel))
    return app
