#!/usr/bin/python
""" the bot package servers as a telegram adapter """
import time
import telegram
import emoji
import os

BOT = telegram.Bot(token=os.env.TELEGRAM_TOKEN)

def send_message(text):
    BOT.send_message(chat_id=os.env.TELEGRAM_CHAT_ID, text=text,
                            parse_mode="Markdown", disable_web_page_preview=True)

