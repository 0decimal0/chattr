import mysql.connector
from mysql.connector import Error

import json

def connect():
    with open('config.json','r') as f:
            data = json.load(f)
    try:
        conn = mysql.connector.connect(host=data["mysql"]["host"],
                database=data["mysql"]["db"],
                user=data["mysql"]["username"],
                password=data["mysql"]["password"])
        '''if conn.is_connected():
            print("database is connected")'''
    except Error as e:
        print(e)
    return conn
'''if __name__=='__main__':
    connect()'''
