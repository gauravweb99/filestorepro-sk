from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "<br><b>😍 Bot is live running</b>"

def run():
  app.run(host='0.0.0.0',port=8080)

def weblive():
    t = Thread(target=run)
    t.start()