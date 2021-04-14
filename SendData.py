import pyodbc
import json
import IDgen
from config import *

with open('event.json') as f:
        data = json.load(f)

#create PYOBDC connection object
cnxn: pyodbc.Connection = pyodbc.connect(coalEngineDBCon.con)
#cursor object from connection
crsr: pyodbc.Cursor = cnxn.cursor()

def postEvent(eventJson):
    try:
        #inject Events
        eventID = IDgen.generateID('event_ID','Events','')
        eventName = eventJson['command']
        # eventCondition = json.dumps(eventJson['conditions'])
        eventCondition = json.dumps(eventJson['conditions'])
        eventSQL = "INSERT INTO [Events] (event_ID,event_Name,event_Condition) VALUES ('{}','{}','{}')".format(eventID,eventName,eventCondition)
        #execute injection
        crsr.execute(eventSQL)
        crsr.commit()

        #inject event true
        trueID = IDgen.generateID('true_ID','Events_True',eventID)
        eventTrue = json.dumps(eventJson['true_part'])
        trueSQL = "INSERT INTO [Events_True] (true_ID,event_ID,true_Argument) VALUES ('{}','{}','{}')".format(trueID,eventID,eventTrue)
        #execute injection
        crsr.execute(trueSQL)
        crsr.commit()

        #inject event false
        falseID = IDgen.generateID('false_ID','Events_False',eventID)
        eventFalse = json.dumps(eventJson['false_part'])
        falseSQL = "INSERT INTO [Events_False] (false_ID,event_ID,false_Argument) VALUES ('{}','{}','{}')".format(falseID,eventID,eventFalse)
        # #execute injection
        crsr.execute(falseSQL)
        crsr.commit()
        cnxn.close()
        return 'Injection success' 
    except pyodbc.Error as err:
        print(err.args[1])
        cnxn.close()
        return 'Error 400: data injection failed'
    except:
        cnxn.close()
        return 'Error 200: code error'

respond = postEvent(data)
print(respond)
