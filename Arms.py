from flask import Flask, render_template, jsonify
import json
from random import choice
from datetime import datetime

# import person
# user = person.user("")

app = Flask(__name__)

#this links is for device 1 
@app.route('/device1', methods=["GET", "POST"])
def Dashoboard():
    user = {
        "username" : "Aman Singh",
        "image":"static/images/amanSingh.jpg"
    }

    devices = [
        {"Dashboard" : "device1",
        "deviceID": "Device1"
        }
    ]
    return render_template('device_dashboard.htm', title='Dashobard', user=user, devices=devices)


#this link is for the main dashboard of the website
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.htm', title='HOME - Landing Page')

@app.route('/overview', methods=['GET', 'POST'])
def overview():
    
    user = {
        "username" : "Aman Singh",
        "image":"static/images/amanSingh.jpg"
    }

    devices = [
        {"Dashboard" : "device1",
        "deviceID": "Device1"
        }
    ]
    return render_template('overview.htm', title='Overview', user=user, devices=devices)
    
#this location will get to the api setting
@app.route('/apisettings', methods=['GET', 'POST'])
def apisettings():
    
    user = {
        "username" : "Aman Singh",
        "image":"static/images/amanSingh.jpg"
    }

    devices = [
        {"Dashboard" : "device1",
        "deviceID": "Device1"
        }
    ]
    return render_template('api_settings.htm', title='API-Settings', user=user, devices=devices)


#this is the testing for api 
@app.route("/api/<string:apikey>/test", methods=["GET", "POST"])
def apitest (apikey):
    return {"data":"working Fine Connected to the api server"}

randlist = [i for i in range(0, 100)]

@app.route("/api/<string:apikey>/temperature", methods=["GET", "POST"])
def get_temperature(apikey):
    
    randData = choice(randlist)
    time = datetime.now()
    time = time.strftime("%H:%M:%S")
    response = [time, randData]
    return jsonify(response)

@app.route("/api/<string:apikey>/moisture", methods=["GET", "POST"])
def get_moisture(apikey):
    
    randData = choice(randlist)
    time = datetime.now()
    time = time.strftime("%H:%M:%S")
    response = [time, randData]
    return jsonify(response)

@app.route("/api/<string:apikey>/humidity", methods=["GET", "POST"])
def get_humidity(apikey):
    
    randData = choice(randlist)
    time = datetime.now()
    time = time.strftime("%H:%M:%S")
    response = [time, randData]
    return jsonify(response)

@app.route("/api/<string:apikey>/light", methods=["GET", "POST"])
def get_light(apikey):
    
    randData = choice(randlist)
    time = datetime.now()
    time = time.strftime("%H:%M:%S")
    response = [time, randData]
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
