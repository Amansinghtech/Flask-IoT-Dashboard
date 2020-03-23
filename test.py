from passlib.hash import sha512_crypt as sha
password = sha.hash("hellboy123")
print(password)
from database import db

mydb = db('aman', '192.168.56.102', 'hacker123', 'ARMS')
query = "update users set password = '{}' where username = 'hellboy'".format(password)

mydb.cursor.execute(query)
mydb.db.commit()