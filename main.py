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

MESSAGE = "{} Ciao {}, benvenutƏ nel gruppo ufficiale dell'[aula break](https://www.youtube.com/watch?v=dQw4w9WgXcQ)."

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
            
            salta = data[0].get('saltaluce') +1
            
            data[0]['saltaluce'] = salta
            with open("main.json", 'w') as jfile:
                json.dump(data, jfile)
            testo = "La corrente è saltata {} volte"
            await message.reply(testo.format(salta), quote=False)
        
        #send audio with message for sburate
        elif message.text.startswith("/amici") or message.text.startswith("/amici@NonFunonziaBot"):
            await message.reply("Addio, Addio, Amici Addio, noi ci dobbiamo sbura-are 💦💦💦", quote=False)
            await message.reply_audio("addio_orso.mp3")
        
        #counter of sburate
        elif message.text.startswith("/sburate") or message.text.startswith("/sburate@NonFunonziaBot"):
           
            with open("main.json", 'r') as jfile:
                data = json.load(jfile)
           
            sburacounter = data[1].get('sburrata')+1
            data[0]['sburrata'] = sburacounter
            
            with open("main.json", 'w') as jfile:
                json.dump(data, jfile)

            testo = "Questo gruppo ha sburato {} volte"
            await message.reply(testo.format(sburacounter), quote=False)

            
        elif message.text.startswith("/momentosbura") or message.text.startswith("/momentosbura@NonFunonziaBot")or message.text.startswith("/momentosburra") or message.text.startswith("/momentosburra@NonFunonziaBot"):
            await message.reply("ATT-T-T-T-ENTƏ ALLA SBURA", quote=False)

        elif message.text.startswith("/ciaoex") or message.text.startswith("/ciaoex@NonFunonziaBot"):
            
            with open("main.json", 'r') as jfile:
                data = json.load(jfile)
           
            excounter = data[2].get('ex')+1
            data[0]['ex'] = excounter
            
            with open("main.json", 'w') as jfile:
                json.dump(data, jfile)

            testo = "Ciao @Ex_Noise, puzzi. Ex è stato salutato {} volte. Diventerà famoso 🧐?"
            await message.reply(testo.format(excounter), quote=False)
        
        


    # comandi admin /infoset
        elif message.text.startswith("/infoset") or message.text.startswith("/infosetcorrente@NonFunziaBot"):
            if message.chat.username == "zAiro12":
                await message.reply("0: luce\n1: sburrata\n2: ex", quote=False)
            else: 
                await message.reply("Non puoi usare questo comando, solo @zAiro12 ha il permesso", quote=False)

        # comandi admin /set [quale si vuole settare] [quanto si vuole settare]
        elif message.text.startswith("/set") or message.text.startswith("/setcorrente@NonFunziaBot"):
            if message.chat.username == "zAiro12":
                val = message.text.split(" ")
                
                with open("main.json", 'r') as jfile:
                    data = json.load(jfile)
                
                if val[1] == '0': 
                    data[0]['saltaluce'] = int(val[2])
                    testo = "La corrente è stata settata a {}"
                    await message.reply(testo.format(int(val[2])), quote=False)
                
                elif val[1] == '1':
                    data[0]['sburrata'] = int(val[2])
                    testo = "Sburrata a {}"
                    await message.reply(testo.format(int(val[2])), quote=False)
                
                elif val[1] == '2':
                    data[0]['ex'] = int(val[2])
                    testo = "ciaoEx a {}"
                    await message.reply(testo.format(int(val[2])), quote=False)
                    
                with open("main.json", 'w') as jfile:
                    json.dump(data, jfile)
                    
            else: 
                await message.reply("Non puoi usare questo comando, solo @zAiro12 ha il permesso", quote=False)


        # comando di prova da non aggiungere ai comandi base e che serve per vedere se il bot è online o pure no
        elif message.text.startswith("/prova") or message.text.startswith("/prova@NonFunonziaBot"):
            await message.reply("ON", quote=False)
            


@app.on_message(filters.new_chat_members)
async def welcome(client, message):
    if(message.new_chat_members[0].username=="NonFunonziaBot"):
       await message.reply("Grazie per avermi aggiunto a questo canale, per ulteriori informazioni scrivi in privato a @zAiro12 o @Ex_Noise")
    else:
        new_members = [u.mention for u in message.new_chat_members]
        text = MESSAGE.format(emoji.SPARKLES, ", ".join(new_members))
        await message.reply_text(text, disable_web_page_preview=True)

print("ONLINE")
app.run()