from flask import Flask, render_template
import json, random

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)
