import requests
from flask import Flask, request # pip install flask
from threading import Thread
from werkzeug.utils import secure_filename

app = Flask('StringToDbDecidaloMap')

@app.route('/')
def home():
  return {"String" : "to", "DbD" : "Map"}

@app.route('/StringToDbDecidaloMap', methods=['POST'])
def StringToDbDecidaloMap():
  if not 'text' in request.form:
    return {"error" : "no text found"}
  text = request.form.get('text')
  
  # Fake Funktion, returnt nur irgendwelche Listen aus dem Text
  # An dieser Stelle wird später eine Referenz Liste oder Tabelle zum Erkennen der Keywords genutzt
  
  DbDecidaloMap = {}
  textSplit = text.split(' ')
  i = 0
  while i < len(textSplit):
    DbDecidaloMap[(textSplit[i])] = ["Matching", "Skills", "For", "Keyword"]
    i += 5

  return DbDecidaloMap

def run():
  app.run(host='0.0.0.0',port=8080)

def start():
    t = Thread(target=run)
    t.start()

start()

print(requests.post("https://stringtoskilllist.shigeocst.repl.co/StringToDbDecidaloMap", data={"text" : "bla bla balds dfs fds fds fds"}).text)