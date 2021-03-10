import logging
import os

from pyrogram import Client, filters


logging.basicConfig(level=logging.INFO, datefmt='%Y/%m/%d %H:%M:%S', format='%(levelname)s: %(message)s')

CHANNELS_LIST = os.getenv('CHANNELS').split(',')
CHAT_IDS = os.getenv('CHAT_IDS').split(',')


@Client.on_message(filters.channel)
async def channel_handler(client, message):
    if message.chat.username in CHANNELS_LIST and not message.edit_date:
        logging.info(message.chat)
        for chat_id in CHAT_IDS:
            await message.forward(chat_id)
