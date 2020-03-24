import json, base64
import urllib.request
from random import choice
import time

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


randlist = [i for i in range(0, 100)]
devlist = ['ARMS1112','ARMS12012','ARMS22212']

while 1:
    try:
        mydata = ['Rosegarden', 'ARMS12012', choice(randlist), choice(randlist), choice(randlist), choice(randlist)]
        a = encode(mydata)
        url = 'http://127.0.0.1/api/aGFja2luZ2lzYWNyaW1lYXNmc2FmZnNhZnNhZmZzYQ==/update/{}'.format(a)
        response = urllib.request.urlopen(url)
        print("[data]: "+ str(mydata))
        print("[Encoded Value]: "+ a)
        print("[url]: "+ url)
        html = response.read()
        print("[output]: " + str(html))
        time.sleep(2)
    except:
        print("Website Not online")
        time.sleep(2)
# mydict = {"name": "Aman Singh", "Age":18}
# a = encode(mydict)
# print(a)
# print(type(a))
# b = decode(a)
# print(b["name"])

# def upload_data():
#     pass