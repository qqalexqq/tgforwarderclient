import logging
import asyncio
from dataclasses import field
from functools import lru_cache
from typing import List

from dataclasses_settings import dataclass_settings
from dataclasses_settings.params import field_params
from pyrogram import Client, filters, handlers

logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y/%m/%d %H:%M:%S",
    format="%(levelname)s: %(message)s",
)


loop = asyncio.get_event_loop()
queues = {}


@dataclass_settings(prefix="bot_")
class Settings:
    api_id: int
    api_hash: str
    channels: List[str]
    chats: List[int]
    session: str = field(metadata=field_params(alias="session_key"))


@lru_cache()
def get_settings() -> Settings:
    return Settings()


def send_media_group(client, media_group_id):
    settings = get_settings()

    for chat_id in settings.chats:
        loop.create_task(client.forward_messages(chat_id, *queues[media_group_id]))


async def channel_handler(client, msg):
    settings = get_settings()
    if msg.chat.username in settings.channels and not msg.edit_date:
        logging.info(msg.chat)

        if hasattr(msg, 'media_group_id') and msg.media_group_id:
            if msg.media_group_id not in queues:
                queues[msg.media_group_id] = (msg.chat.id, [])
                loop.call_later(10, send_media_group, client, msg.media_group_id)

            queues[msg.media_group_id][1].append(msg.message_id)
        else:
            for chat_id in settings.chats:
                await msg.forward(chat_id)


def main():
    settings = get_settings()
    app = Client(settings.session, settings.api_id, settings.api_hash)
    app.add_handler(handlers.MessageHandler(channel_handler, filters.channel))
    app.run()


if __name__ == "__main__":
    main()
