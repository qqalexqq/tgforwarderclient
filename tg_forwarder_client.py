import logging
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


async def channel_handler(_, message):
    settings = get_settings()
    if message.chat.username in settings.channels and not message.edit_date:
        logging.info(message.chat)
        for chat_id in settings.chats:
            await message.forward(chat_id)


def main():
    settings = get_settings()
    app = Client(settings.session, settings.api_id, settings.api_hash)
    app.add_handler(handlers.MessageHandler(channel_handler, filters.channel))
    app.run()


if __name__ == "__main__":
    main()
