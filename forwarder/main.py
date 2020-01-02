"""Main module for telegram forwarder bot."""
import logging

from pyrogram import Client, Filters


logging.basicConfig(level=logging.INFO, datefmt='%Y/%m/%d %H:%M:%S', format='%(levelname)s: %(message)s')

CHANNELS_LIST = ['addmeto', 'techsparks', 'g33ks', 'blognot', 'radiotnews']
CHAT_ID = -1001005702961


app = Client('forwarder_account')


@app.on_message(Filters.channel)
def channel_handler(client, message):
    if message.chat.username in CHANNELS_LIST:
        logging.info(message.chat)
        message.forward(CHAT_ID)


app.run()
