from database import db
import hashlib
from passlib.hash import sha512_crypt as sha
from datetime import datetime

class user:

    def __init__(self, username, password):
        self.db = db('aman', '192.168.56.102', 'hacker123', 'ARMS')
        self.username = username 
        self.secret = password
        self.authenticated = False
        self.auth()
        self.get_details()
        self.get_devices()

    def auth (self):
        #this is the place where user will get authenticated
        try:
            query = 'select password from users where username = "{0}"'.format(self.username)
            self.db.cursor.execute(query)
            output = self.db.cursor.fetchall()
            if sha.verify(self.secret, output[0][0]):
                self.authenticated = True
                
                query = 'update users set last_login = now() where username = "{0}";'.format(self.username)
                self.db.cursor.execute(query)
                self.db.db.commit()

                return True
            else:
                self.authenticated = False
                return False

        except Exception as e:
            print("[ERROR!]")
            print(e)

    def get_details (self):
        
        try:
            if self.authenticated:
                query = 'select * from users where username = "{0}"'.format(self.username)
                self.db.cursor.execute(query)
                output = self.db.cursor.fetchall()
                output = output[0]
                self.first = output[2]
                self.last = output[3]
                self.email = output[4]
                self.phone = output[5]
                self.last_login = output[6].strftime("%d-%b-%Y (%H:%M:%S.%f)")
                self.api = output[7]
                return True

            else:
                print("User not logged in!")
                return False

        except Exception as e:
            print("ERROR!")
            print(e)
    
    def get_devices(self):

        try:
            if self.authenticated:
                query = 'select deviceID from Node where username = "{0}"'.format(self.username)
                self.db.cursor.execute(query)
                output = self.db.cursor.fetchall()
                dummy = []
                for dev in output:
                    dummy.append(dev[0])
                self.device_list = dummy
                return dummy
            else:
                return False

        except Exception as e:
            print("[Error!]")
            print (e)

    def dev_info(self, deviceID):
        try:
            
            if self.authenticated:
                self.db.db.commit()
                query = 'select * from Node where deviceID="{0}";'.format(deviceID)
                self.db.cursor.execute(query)
                output = self.db.cursor.fetchall()
                print(output)
                return output[0]
            else:
                return False

        except Exception as e:
            print('[ERROR!]')
            print(e)
    
    def field_values(self, fieldname):
        #here we will access all the values of devices according to time
        try:
            if self.authenticated:
                query = 'select * from (select * from {0} order by date_time desc limit 10) dummy order by date_time asc;'.format(fieldname)
                self.db.cursor.execute(query)
                output = self.db.cursor.fetchall()
                return output
            else:
                return False
        except Exception as e:
            print('[ERROR!]')
            print(e)

    def device_values(self, fieldname, deviceID):
        try:
            if self.authenticated:
                query = 'select * from (select * from (select * from {0} where deviceID = "{1}") var1 order by date_time desc limit 10) dummy order by date_time asc;'.format(fieldname, deviceID)
                self.db.cursor.execute(query)
                output = self.db.cursor.fetchall()
                # print(output)
                return output
            else:
                return False

        except Exception as e:
            print('[ERROR!]')
            print(e)

#testing side for the class
# test = user("hellboy", "hello world")
# test.get_details()
# print(test.get_devices())
# print(test.dev_info("ARMS1112"))
# print(test.field_values('Rosegarden'))
# print(test.device_values("Rosegarden", "ARMS12012"))