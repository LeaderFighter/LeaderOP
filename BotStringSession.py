# MafiaBot Support

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""MafiaBot TG-Bot Support String Session
Login Using Your Telegram Bot
Enter TG-Bot Token, Get Bot Token From @BotFather""")
APP_ID = "2857558"
API_HASH = "1038be815e038592fa2b483c13dd6c4b"

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())