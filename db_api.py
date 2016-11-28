import sqlite3
from datetime import date, datetime

class dbClass:
    def __init__(self):
        '''Open DB connection.'''
        self.conn = sqlite3.connect('my.db')
        print "Opened database successfully";
        self.cursor = self.conn.cursor()


    def createTable(self):
        try:
            self.cursor.execute('''DROP TABLE AQI''')
            self.conn.commit()
        except:
            print "Could not drop table"
        try:
            self.cursor.execute('''CREATE TABLE AQI
                   (
                   CREATE_DATE          DATE,
                   AQI_TOTAL            INT     ,
                   AQI_OZONE            INT             ,
                   AQI_PM_25            INT             ,
                   AQI_PM_10            INT             ,
                   AQI_MSG        CHAR(200));''')
            print "Table created successfully"
            self.conn.commit()
        except:
            print "Table already exists."


    def addEntry(self, aqi_total, aqi_msg):
        today = date.today()
        try:
            self.cursor.execute('''INSERT INTO AQI(CREATE_DATE, AQI_TOTAL, AQI_MSG) VALUES (?, ?, ?)''',\
            (today, aqi_total, aqi_msg))
            self.conn.commit()
            print "Record created successfully";
        except:
            print "Error inserting record"
            self.conn.rollback()


    def getEntry(self):
        try:
            return self.cursor.execute('''SELECT CREATE_DATE, AQI_TOTAL, AQI_MSG FROM AQI''')
        except:
            self.conn.rollback()

    def closeDB(self):
        self.conn.close()
