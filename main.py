import json
from flask import Flask, request # pip install flask
from threading import Thread

app = Flask('StringToDbDecidaloMap')

@app.route('/')
def home():
  return {"String" : "to","DbD" : "Map"}

@app.route('/StringToDbDecidaloMap', methods=['POST'])
def StringToDbDecidaloMap():
  if not 'text' in request.form:
    return {"error" : "no text found"}
  text = request.form.get('text')
  
  # An dieser Stelle wird eine Referenz Tabelle zum Erkennen der Keywords genutzt
  with open("TranslationDict.json", "r") as td:
    DbDecidaloMap = json.load(td)

    # kürzen der Tabelle auf Anwendungsbezogene Länge
    anforderungenToRemove = []

    # Anforderung nicht im Ausschreibungstext? -> raus damit
    for Anforderung in DbDecidaloMap:
      if not Anforderung.lower() in text.lower():
        anforderungenToRemove.append(Anforderung)

    for anforderungR in anforderungenToRemove:
      del DbDecidaloMap[anforderungR]

    return DbDecidaloMap
    

def run():
  app.run(host='0.0.0.0',port=8080)

def start():
    t = Thread(target=run)
    t.start()

start()