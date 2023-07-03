import mysql.connector

dataBase= mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
)

#prepare a cursor object
cursorObject = dataBase.cursor()
#createdatabase

cursorObject.execute("CREATE DATABASE crm")
print('all done!!')