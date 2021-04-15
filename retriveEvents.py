import pyodbc
import json
import re
from config import *

#create PYOBDC connection object
cnxn: pyodbc.Connection = pyodbc.connect(coalEngineDBCon.con)
#cursor object from connection
crsr: pyodbc.Cursor = cnxn.cursor()

def getEvent(eventID):
    #select query
    select_sql = "SELECT event_Condition From Events WHERE event_ID = '{}'".format(eventID)
    #execute select query
    crsr.execute(select_sql)
    rows = crsr.fetchall()
    # Close db connetion
    cnxn.close()

    #conver to JSON serializable
    data=[]
    data.append([x for x in rows])
    return data

eventResult = getEvent('2c0unr2ntl')

str1 = ''.join(str(e) for e in eventResult)
m = re.findall('{(?:[^{}])*}',str1)
for item in m:
    print(item)
my_lst_string = ','.join(map(str,m))
print(my_lst_string)
y = json.loads(my_lst_string)
print(y['arguments'])