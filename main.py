from pyrogram import Client, filters, emoji
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()


app = Client(
    "my_account",
    app_version="1.1.1",
    device_model="PC",
    system_version="Mac",
    lang_code="it",
    api_id=os.getenv('api_id'), 
    api_hash=os.getenv('api_hash'),
    bot_token=os.getenv('bot_token')
)

MESSAGE = "{} Ciao {}, benvenut* nel gruppo ufficiale dell'[aula break](https://www.youtube.com/watch?v=dQw4w9WgXcQ)."

@app.on_message(filters.text)
async def command(client, message):
    if message.text == "/start" or message.text == "/start@NonFunonziaBot":
        await message.reply("Grazie per avremi aggiunto. Per tutte le informazioni relative a questo bot chiedere a @zAiro12")
    elif message.text == "/momentogubbio" or message.text == "/momentogubbio@NonFunonziaBot":
        await message.reply("Vuoi che ti porti la carta igienica? O la laurea se vuoi tanto è uguale 😂")


@app.on_message(filters.new_chat_members)
async def welcome(client, message):
    #print(message.new_chat_members[0].username)
    if(message.new_chat_members[0].username=="NonFunonziaBot"):
       await message.reply("Grazie per avermi aggiunto a questo canale, per ulteriori informazioni scrivi in privato a @zAiro12")
    else:
        new_members = [u.mention for u in message.new_chat_members]
        text = MESSAGE.format(emoji.SPARKLES, ", ".join(new_members))
        await message.reply_text(text, disable_web_page_preview=True)

print("ON")
app.run()