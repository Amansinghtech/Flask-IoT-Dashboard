import json
import base64
#decoding and encoding data is possible via base64 library so we are going to use this method to update values
def convert(data):
    return json.dumps(data)

def deconvert(data):
    return json.loads(data)

mydict = {"name": "Aman Singh", "Age":18}
# mydict = ["Aman", "singh", 18]

def base_encode(message):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

def base_decode(base64_message):
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message

data = convert(mydict)

print(data)

encoded_data = base_encode(data)

print(encoded_data)

new_data = base_decode(encoded_data)

print(new_data)

new_dict = deconvert(new_data)

print(new_dict["name"])

print(type(mydict) is dict)