from flask import Flask, render_template, jsonify, redirect, request
import json, database, base64
from random import choice
from datetime import datetime
import person
import os, binascii

app = Flask(__name__)

logged_in = {}
api_loggers = {}
mydb = database.db('aman', '192.168.56.102', 'hacker123', 'ARMS')

#test api key aGFja2luZ2lzYWNyaW1lYXNmc2FmZnNhZnNhZmZzYQ==


@app.route("/login", methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        user = person.user(request.form['username'], request.form['password'])
        if user.authenticated:
            user.session_id = str(binascii.b2a_hex(os.urandom(15)))
            logged_in[user.username] = {"object": user}
            return redirect('/overview/{}/{}'.format(request.form['username'], user.session_id))
        else:
            error = "invalid Username or Passowrd"
       
    return render_template('Login.htm', error=error)
    
#this links is for device 1 
@app.route('/device1/<string:username>/<string:session>', methods=["GET", "POST"])
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

@app.route('/overview/<string:username>/<string:session>', methods=['GET', 'POST'])
def overview(username, session):
    
    global logged_in

    if username in logged_in and (logged_in[username]['object'].session_id == session):
        user = {
            "username" : username,
            "image":"/static/images/amanSingh.jpg",
            "api": logged_in[username]["object"].api,
            "session" : session
        }

        devices = [
            {"Dashboard" : "device1",
            "deviceID": "Device1"
            }
        ]
        return render_template('overview.htm', title='Overview', user=user, devices=devices)
    
    else:
        return redirect('/login')
        
#this location will get to the api setting
@app.route('/apisettings/<string:username>/<string:session>', methods=['GET', 'POST'])
def apisettings(username, session):
    
    global logged_in

    if username in logged_in and (logged_in[username]['object'].session_id == session):
        user = {
            "username" : username,
            "image":"/static/images/amanSingh.jpg",
            "api": logged_in[username]["object"].api,
            "session" : session
        }

        devices = [
            {"Dashboard" : "device1",
            "deviceID": "Device1"
            }
        ]
        return render_template('api_settings.htm', title='API-Settings', user=user, devices=devices)
    
    else:
        return redirect('/login')


#this part is for the profile view
@app.route('/profile/<string:username>/<string:session>', methods=['GET', 'POST'])
def profile(username, session):
    
    global logged_in

    if username in logged_in and (logged_in[username]['object'].session_id == session):
        user = {
            "username" : username,
            "image":"/static/images/amanSingh.jpg",
            "api": logged_in[username]["object"].api,
            "session" : session,
            "firstname": logged_in[username]["object"].first,
            "lastname": logged_in[username]["object"].last,
            "email":logged_in[username]["object"].email,
            "phone":logged_in[username]["object"].phone,
            "lastlogin":logged_in[username]["object"].last_login,
        }

        devices = [
            {"Dashboard" : "device1",
            "deviceID": "ARMS12012"
            }
        ]
        return render_template('profile.htm', title='API-Settings', user=user, devices=devices)
    
    else:
        return redirect('/login')


@app.route('/logout/<string:username>/<string:session>', methods=['GET', 'POST'])
def logout(username, session):
    
    global logged_in

    if username in logged_in and (logged_in[username]['object'].session_id == session):
        logged_in.pop(username)
        # print("logged out")
        return redirect('/')
    else:
        return redirect('/login')



#this is the testing for api 
@app.route("/api/<string:apikey>/test", methods=["GET", "POST"])
def apitest (apikey):
    return {"data":"working Fine Connected to the api server"}


#get all the devices information from the user
@app.route("/api/<string:apikey>/listdevices", methods=['GET', 'POST'])
def listdevices(apikey):
    global api_loggers
    global mydb
    if not(apikey in api_loggers):
        try:
            query = "select username from users where api_key = '{}'".format(apikey)
            mydb.cursor.execute(query)
            username = mydb.cursor.fetchall()
            username = username[0][0]
            apiuser = person.user(username, "dummy")
            apiuser.authenticated = True
            devices_list = apiuser.get_devices()
            api_loggers[apikey] = {"object" : apiuser}
            return jsonify(devices_list)
        except Exception as e:
            print (e)
            return jsonify({"data":"Oops Looks like api is not correct"})
    
    else:
        data = api_loggers[apikey]["object"].get_devices()
        return jsonify (data)

randlist = [i for i in range(0, 100)]

@app.route('/api/<string:apikey>/deviceinfo/<string:deviceID>', methods=['GET', 'POST'])
def device_info (apikey, deviceID):
    global api_loggers
    global mydb
    if not(apikey in api_loggers):
        try:
            query = "select username from users where api_key = '{}'".format(apikey)
            mydb.cursor.execute(query)
            username = mydb.cursor.fetchall()
            username = username[0][0]
            apiuser = person.user(username, "dummy")
            apiuser.authenticated = True
            data = apiuser.dev_info(deviceID)
            api_loggers[apikey] = {"object" : apiuser}
            #this part is hard coded so remove after fixing the issue
            data = list(data)
            data[2] = "Rosegarden"
            return jsonify(data)
        except Exception as e:
            print (e)
            return jsonify({"data":"Oops Looks like api is not correct"})
    
    else:
        data = api_loggers[apikey]["object"].dev_info(deviceID)

        #this part is hard coded so remove after fixing the issue
        data = list(data)
        data[2] = "Rosegarden"
        return jsonify (data)

@app.route('/api/<string:apikey>/fieldstat/<string:fieldname>', methods=['GET', 'POST'])
def fieldstat (apikey, fieldname):
    
    global api_loggers
    global mydb
    if not(apikey in api_loggers):
        try:
            query = "select username from users where api_key = '{}'".format(apikey)
            mydb.cursor.execute(query)
            username = mydb.cursor.fetchall()
            username = username[0][0]
            apiuser = person.user(username, "dummy")
            apiuser.authenticated = True
            data = apiuser.field_values(fieldname)
            api_loggers[apikey] = {"object" : apiuser}
            return jsonify(data)
        except Exception as e:
            print (e)
            return jsonify({"data":"Oops Looks like api is not correct"})
    
    else:
        data = api_loggers[apikey]["object"].field_values(fieldname)
        return jsonify (data)


@app.route('/api/<string:apikey>/devicestat/<string:fieldname>/<string:deviceID>', methods=['GET', 'POST'])
def devicestat (apikey, fieldname, deviceID):
    
    global api_loggers
    global mydb
    if not(apikey in api_loggers):
        try:
            query = "select username from users where api_key = '{}'".format(apikey)
            mydb.cursor.execute(query)
            username = mydb.cursor.fetchall()
            username = username[0][0]
            apiuser = person.user(username, "dummy")
            apiuser.authenticated = True
            data = apiuser.device_values(fieldname, deviceID)
            api_loggers[apikey] = {"object" : apiuser}
            return jsonify(data)
        except Exception as e:
            print (e)
            return jsonify({"data":"Oops Looks like api is not correct"})
    
    else:
        data = api_loggers[apikey]["object"].device_values(fieldname, deviceID)
        return jsonify (data)

@app.route('/api/<string:apikey>/update/<string:data>', methods=['GET','POST'])
def update_values(apikey, data):
    global mydb
    try:
        data = decode(data)
        output = mydb.get_apikeys()
        if apikey in output:
            if (len(data) == 6) and (type(data) is list):
                fieldname = data[0]
                deviceID = data[1]
                temp = data[2]
                humidity = data[3]
                moisture = data[4]
                light = data[5]
                mydb.update_values(apikey, fieldname, deviceID, temp, humidity, moisture, light)
                return ("Values Updated")
            else:
                return "Data Decoding Error!"
        else:
            return "Api key invalid"

    except Exception as e:
        print (e)
        return jsonify({"data":"Oops Looks like api is not correct"})


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


def encode(data):
    data = json.dumps(data)
    message_bytes = data.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

def decode(base64_message):
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return json.loads(message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port = "80", debug=True)
