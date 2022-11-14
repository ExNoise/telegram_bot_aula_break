from pyrogram import Client, filters, emoji
from dotenv import load_dotenv
import os
import json

def configure():
    load_dotenv()

app = Client(
    "my_account",
    app_version="1.3.0",
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

    ## LOGS ##
    if message.text.startswith('/'):
        print(message.chat.username, "IN", message.chat.id,"\ntext:", message.text)

    ## COMMAND ##
    if message.text == "/start" or message.text == "/start@NonFunonziaBot":
        await message.reply("Grazie per avermi aggiunto a questo canale, per ulteriori informazioni scrivi in privato a @zAiro12", quote=False)
    
    elif message.text == "/momentogubbio" or message.text == "/momentogubbio@NonFunonziaBot":
        await message.reply("Vuoi che ti porti la carta igienica? O la laurea se vuoi tanto è uguale 😂", quote=False)
    
    elif message.text == "/correntesaltata" or message.text == "/correntesaltata@NonFunonziaBot":
        with open("main.json", 'r') as jfile:
            data = json.load(jfile)
        
        saltaluce = int(data["saltaluce"])+1
        
        data['saltaluce'] = saltaluce
        with open("main.json", 'w') as jfile:
            json.dump(data, jfile)
        testo = "La corrente è saltata {} volte"
        await message.reply(testo.format(saltaluce), quote=False)

    elif message.text.startswith("/setcorrente") or message.text.startswith("/setcorrente@NonFunziaBot"):
        if message.chat.username == "zAiro12":
            val = message.text.split(" ")
            with open("main.json", 'r') as jfile:
                data = json.load(jfile)
                
            data['saltaluce'] = int(val[1])
                
            with open("main.json", 'w') as jfile:
                json.dump(data, jfile)
            testo = "La corrente è stata settata a {}"
            await message.reply(testo.format(int(val[1])), quote=False)
        else: 
            await message.reply("Non puoi usare questo comando, solo @zAiro12 ha il permesso", quote=False)

@app.on_message(filters.new_chat_members)
async def welcome(client, message):
    if(message.new_chat_members[0].username=="NonFunonziaBot"):
       await message.reply("Grazie per avermi aggiunto a questo canale, per ulteriori informazioni scrivi in privato a @zAiro12")
    else:
        new_members = [u.mention for u in message.new_chat_members]
        text = MESSAGE.format(emoji.SPARKLES, ", ".join(new_members))
        await message.reply_text(text, disable_web_page_preview=True)

print("ON")
app.run()