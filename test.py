from database import db
import time
mydb = db('aman', '192.168.56.102', 'hacker123', 'ARMS')
for i in range(10):
    query = 'insert into Rosegarden (deviceID, temperature, humidity, moisture, light, date_time) values("ARMS1112", {0}, {1}, {2}, {3}, now());'.format((i+10),(i+20),(i+14),(i+60))
    mydb.cursor.execute(query)
    mydb.db.commit()
    print(query)
    time.sleep(5)