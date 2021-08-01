import logging
import os

from pyrogram import Client, filters, handlers

logging.basicConfig(level=logging.INFO, datefmt="%Y/%m/%d %H:%M:%S", format="%(levelname)s: %(message)s")

CHANNELS_LIST = os.getenv("CHANNELS").split(",")
CHAT_IDS = [int(chat_id) for chat_id in os.getenv("CHAT_IDS").split(",")]
SESSION_STRING = os.getenv("SESSION_KEY", "bot_session")


async def channel_handler(_, message):
    if message.chat.username in CHANNELS_LIST and not message.edit_date:
        logging.info(message.chat)
        for chat_id in CHAT_IDS:
            await message.forward(chat_id)


def main():
    app = Client(SESSION_STRING, os.getenv('API_ID'), os.getenv('API_HASH'))

    app.add_handler(handlers.MessageHandler(channel_handler, filters.channel))
    app.run()


if __name__ == "__main__":
    main()
