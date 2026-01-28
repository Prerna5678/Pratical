import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="username@2811",
        database="Library"
    )

'''
import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="username@2811",      
    database="Library"
)

connection.close()
'''