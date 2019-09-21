import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="root")

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES;")

for db in mycursor:
    print("database is:", db)
    
    
demodb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="demo")

demoCursor = demodb.cursor()

demoCursor.execute("SELECT * FROM user;")

for user in demoCursor:
    print("User:", user)
    
    
demodb2 = mysql.connector.connect(host="localhost", user="root", passwd="root", database="demo")

demoCursor2 = demodb2.cursor()

demoCursor2.execute("SELECT * FROM user;")

result = demoCursor2.fetchall()

for usr in result:
    print("usr:", usr)
    
    
    
demodb3 = mysql.connector.connect(host="localhost", user="root", passwd="root", database="demo")

demoCursor3 = demodb3.cursor()

demoCursor3.execute("SELECT * FROM user;")

row = demoCursor3.fetchone()
for detail in row:
    print("details:", detail)