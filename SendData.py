import pyodbc
import json
import IDgen
from config import *

def postEvent(eventJson,eventID):
    try:
        #create PYOBDC connection object
        cnxn: pyodbc.Connection = pyodbc.connect(coalEngineDBCon.con)
        #cursor object from connection
        crsr: pyodbc.Cursor = cnxn.cursor()
        #inject Events
        eventName = eventJson['command']
        # eventCondition = json.dumps(eventJson['conditions'])
        eventCondition = json.dumps(eventJson['conditions'])
        eventSQL = "INSERT INTO [Events] (event_ID,event_Name,event_Condition) VALUES ('{}','{}','{}')".format(eventID,eventName,eventCondition)
        #execute injection
        crsr.execute(eventSQL)
        crsr.commit()
        cnxn.close()
        return 'Injection success'
    #error handler
    except pyodbc.Error as err:
        for error in err:
            print(err.args[error])
        cnxn.close()
        return 'Error 400: data injection failed'
    except:
        cnxn.close()
        return 'Error 200: code error'

def postTrue(trueJson,eventID):
    try:
        #create PYOBDC connection object
        cnxn: pyodbc.Connection = pyodbc.connect(coalEngineDBCon.con)
        #cursor object from connection
        crsr: pyodbc.Cursor = cnxn.cursor()
        #inject event true
        trueID = IDgen.generateID('true_ID','Events_True',eventID)
        eventTrue = json.dumps(trueJson['true_part'])
        trueSQL = "INSERT INTO [Events_True] (true_ID,event_ID,true_Argument) VALUES ('{}','{}','{}')".format(trueID,eventID,eventTrue)
        #execute injection
        crsr.execute(trueSQL)
        crsr.commit()
        cnxn.close()
        return 'Injection success'
    #error handler
    except pyodbc.Error as err:
        print(err.args[1])
        cnxn.close()
        return 'Error 400: data injection failed'
    except:
        cnxn.close()
        return 'Error 200: code error'
    
def postFalse(falseJson,eventID):
    try:
        #create PYOBDC connection object
        cnxn: pyodbc.Connection = pyodbc.connect(coalEngineDBCon.con)
        #cursor object from connection
        crsr: pyodbc.Cursor = cnxn.cursor()
        #inject event false
        falseID = IDgen.generateID('false_ID','Events_False',eventID)
        eventFalse = json.dumps(falseJson['false_part'])
        falseSQL = "INSERT INTO [Events_False] (false_ID,event_ID,false_Argument) VALUES ('{}','{}','{}')".format(falseID,eventID,eventFalse)
        # #execute injection
        crsr.execute(falseSQL)
        crsr.commit()
        cnxn.close()
        return 'Injection success'
    #error handler
    except pyodbc.Error as err:
        print(err.args[1])
        cnxn.close()
        return 'Error 400: data injection failed'
    except:
        cnxn.close()
        return 'Error 200: code error'

def sendDataTestrun():
    with open('event.json') as f:
        data = json.load(f)
    eventID = IDgen.generateID('event_ID','Events','')
    result1 = postEvent(data,eventID)
    result3 = postTrue(data,eventID)
    result2 = postFalse(data,eventID)

    print(result1)
    print(result2)
    print(result3)

#test
sendDataTestrun()