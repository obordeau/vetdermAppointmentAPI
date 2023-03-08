import requests
from flask import Flask, jsonify
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)
 
def numberToMonth(x):
    months = {
        "01": "Janvier",
        "02": "Février",
        "03": "Mars",
        "04": "Avril",
        "05": "Mai",
        "06": "Juin",
        "07": "Juillet",
        "08": "Août", 
        "09": "Septembre",
        "10": "Octobre",
        "11": "Novembre",
        "12": "Décembre"
        }
    return months[x]

def addFirstWord(day,month,year):
    today = datetime.datetime.now()
    appointment = datetime.datetime(int(year), int(month), int(day))
    
    delta = appointment - today

    if (delta.days + 1 == 0):
        return "AUJOURD'HUI "
    elif (delta.days + 1 == 1):
        return "DEMAIN "
    elif (delta.days + 1 == 2):
        return "APRES-DEMAIN "
    elif (delta.days + 1 >= 3 and delta.days + 1 <= 7):
        return "CE "
    else: 
        return ""

def getFirst(x):
    for item in x:
        if len(item) > 0:
            return item
    return False

@app.route("/")
def first_appointment():
    # paramsPost = {
    # "api_key": "tGa-zibffSpW",
    # }
    # r = requests.post("https://www.parsehub.com/api/v2/projects/ty4Pdcv2K3hO/run", data=paramsPost)

    # paramsGet = {
    # "api_key": "tGa-zibffSpW",
    # "format": "json"
    # }
    # r = requests.get('https://www.parsehub.com/api/v2/projects/ty4Pdcv2K3hO/last_ready_run/data', params=paramsGet)
    
    # r =  r.json()
    # r = getFirst(r["buttons"])
    
    # if not(r):
    #     return ""

    # litteralDay,date = r["date"].split(", ")
    # day,month,year = date.split("-")
    
    # result = {
    #     "date" : addFirstWord(day,month,year) + litteralDay + " " + day + " " + numberToMonth(month),
    #     "time" : r["time"].replace(":", "h")
    # }
    
    result = {
        "date" : "Vendredi 24 Mars",
        "time" : "12h40"
    }
    
    return jsonify(result)