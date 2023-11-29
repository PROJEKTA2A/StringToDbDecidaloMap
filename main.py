import requests
from flask import Flask, request # pip install flask
from threading import Thread
from werkzeug.utils import secure_filename

app = Flask('StringToSkillList')

@app.route('/')
def home():
  return {"String" : "to", "Skill" : "List"}

@app.route('/StringToSkillList', methods=['POST'])
def StringToSkillList():
  if not 'text' in request.form:
    return {"error" : "no text found"}
  text = request.form.get('text')

  # Fake Funktion, returnt nur irgendwelche Listen aus dem Text
  ListeAnforderungen = []
  textSplit = text.split(' ')
  i = 0
  while i < len(textSplit):
    ListeAnforderungen.append(textSplit[i])
    i += 5

  return {"ListeAnforderungen" : ListeAnforderungen,
         "decidaloMatchList" : textSplit}

def run():
  app.run(host='0.0.0.0',port=8080)

def start():
    t = Thread(target=run)
    t.start()

start()