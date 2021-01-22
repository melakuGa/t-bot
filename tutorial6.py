#webhook heroku - this tutorial works on cloud. 
#   to run flask on local server
#       export FLASK_APP=tutorial6
#       flask run
#https://github.com/python-telegram-bot/python-telegram-bot/wiki/Where-to-host-Telegram-Bots#vps
#https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks
#https://python-telegram-bot.readthedocs.io/
#https://seminar.io/2018/09/03/building-serverless-telegram-bot/
#https://www.heroku.com/
from flask import Flask, render_template, request

import os
import telegram
import pafy

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def webhook():
    bot = telegram.Bot(token=os.environ["YOURAPIKEY"])
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id     = update.effective_chat.id
        text        = update.message.text
        #vid         =pafy.new(str(text))
        #vidttl      = str(vid.title)
        #audio       = vid.getbestaudio()
        audioUrl    = "https://r3---sn-xuj-5qqs.googlevideo.com/videoplayback?expire=1611349301&ei=1egKYPC6FI6ixN8PwNa9UA&ip=196.190.191.129&id=o-AGO-Mw5iR3sA8vpJ9hh1D-aes38YbwfHB9dw7qJf4LOc&itag=251&source=youtube&requiressl=yes&mh=Hj&mm=31,29&mn=sn-xuj-5qqs,sn-5hne6nlk&ms=au,rdu&mv=m&mvi=3&pl=19&initcwndbps=88750&vprv=1&mime=audio/webm&ns=HiznOq4nflonKXh-SdbhwbIF&gir=yes&clen=6008659&otfp=1&dur=386.301&lmt=1594755824977662&mt=1611327402&fvip=3&keepalive=yes&c=WEB&txp=6211222&n=KRPPA1g0iSvMz9w&sparams=expire,ei,ip,id,itag,source,requiressl,vprv,mime,ns,gir,clen,otfp,dur,lmt&lsparams=mh,mm,mn,ms,mv,mvi,pl,initcwndbps&lsig=AG3C_xAwRAIgWLfu8-FEJmiIrRXDwdSsBBwvnLrsCrs6I1LmPnVgrY4CICVQIJ9V1geqkE2QfSM5KpAzYv9cDAT4ldfuJDptFTEs&sig=AOq0QJ8wRQIhAMG_pE2fUK6VAWE6kg3QPJz5QNITSt-aQE8Up6vVPlorAiBZYYJb568wbaH7UFTK4AQAebiww1KwkQB6L56VRqL7Jg==&ratebypass=yes"
        
        first_name  = update.effective_chat.first_name
        user = update.effective_chat.username
        
        # Reply with the same message
        #bot.sendMessage(chat_id=chat_id, text=f"{vidttl}{audioUrl}")
        bot.sendAudio(chat_id = chat_id, audio = audioUrl)
        return 'ok'
    return 'error'

def index():
    return webhook()
