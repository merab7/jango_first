import mysql.connector
import os


dataBase =mysql.connector.connect(user='root',
                                passwd=os.environ.get('MYSQLPASS'),
                              host='localhost',
                                )

#prepare a cursor object
cursorObject = dataBase.cursor()

#crate a database
cursorObject.execute('CREATE DATABASE elderco')