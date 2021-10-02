#!/usr/bin/python
""" the bot package servers as a telegram adapter """
import telegram
import os
import random
from dotenv import load_dotenv

load_dotenv()

BOT = telegram.Bot(token=os.getenv("TELEGRAM_TOKEN"))

messages = {
    # hiring
    "hiring_general": "VACentral is hiring! Check out https://vacentral.org#roles to see all active roles!",
    "hiring_software": "Software Developer with experience in Typescript, Reactjs, Nextjs, Chakra-UI, Python and GraphQL? Apply today at https://vacentral.org#roles-software",
    "hiring_social": "Social Media Manager with experience in Tik Tok, Telegram, Instagram, Facebook, Twitter, Pinterest, or Linkedin? Apply today at https://vacentral.org#roles-social",
    "hiring_graphics": "Graphic Designer with experience in Canva, Adobe Creative Suite, Figma, UI/UX Design, Vector Graphics? Apply today at https://vacentral.org#roles-design",
    "hiring_writing": "Copy and Content Writer with experience in writing Articles, Landing Copy, Newsletters, Promotions, Social Media Posts? Apply today at https://vacentral.org#roles-writing",
    "hiring_leaders": "Product or Project Manager with experience using Coda, Discord, Automation, Kanban, Agile Methodology? Apply today at https://vacentral.org#roles-leader",
    "hiring_video": "Viral Video Content creators with experience in Tik Tok, YouTube, Webinars, Advertising, and Courses? Apply today at https://vacentral.org#roles-video",
    "hiring_assistant": "Personal Assistants with experience in Scheduling, Scribing, Organization, HR, Onboarding, and Commnity Management with Discord? Apply today at https://vacentral.org#roles-assistants",
    "hiring_sales": "Sales and Marketing minded person with experience in Cold Outreach, Automation, Advertising, CRM, and Growth Hacking? Apply today at https://vacentral.org#roles-sales",
    "hiring_ecomm": "eCommerce Managers with experience in Amazon, Shopify, Dropshipping, Fulfilment, Brand Strategy? Apply today at https://vacentral.org#roles-ecomm",

    # courses
}


def send_message(text):
    BOT.send_message(chat_id=os.getenv("TELEGRAM_CHAT_ID"), text=text,
                     parse_mode="Markdown", disable_web_page_preview=True)


def send_random_message():
    key, text = random.choice(list(messages.items()))
    send_message(text=text)
