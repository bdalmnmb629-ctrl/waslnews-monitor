from telethon import TelegramClient, events
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

client = TelegramClient("session", API_ID, API_HASH)

CHANNEL = "waslnews"
KEYWORD = "الموجز"

@client.on(events.NewMessage(chats=CHANNEL))
async def handler(event):
    text = event.raw_text or ""

    if KEYWORD in text:
        print("تم العثور على الموجز:")
        print(text)
        # هنا لاحقًا هنضيف إرسال الإشعار

print("بدأت مراقبة قناة وصل للأخبار...")

client.start()
client.run_until_disconnected()
