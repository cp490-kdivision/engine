import pyodbc
import json
import uuid
from config import *

def postEvent(eventJSON,eventID):
    try:
        #condition's variable
        conditionID = uuid.uuid4()
        #create PYOBDC connection object
        cnxn: pyodbc.Connection = pyodbc.connect(coalEngineDBCon.con)
        #cursor object from connection
        crsr: pyodbc.Cursor = cnxn.cursor()
        #event condition JSON
        condition = eventJSON['conditions']
        eventName = eventJSON['command']
        #inject new event
        eventSQL = "INSERT INTO [Events] (event_ID,event_Name) VALUES ('{}','{}')".format(eventID,eventName)
        crsr.execute(eventSQL)
        crsr.commit()
        #inject primities
        primitivesSQL = "INSERT INTO [Event_Condition] (condition_ID,event_ID) VALUES ('{}','{}')".format(conditionID,eventID)
        crsr.execute(primitivesSQL)
        crsr.commit()
        #extract primitive and argument
        for i in range(len(condition)):
            primitives = condition[i].get('primitive')
            args = condition[i].get('arguments')
            #inject argument
            argsSQL = "INSERT INTO [ConfitionArg] (condition_ID,condition_Arg,Condition_Primitive) VALUES ('{}','{}','{}')".format(conditionID,json.dumps(args),json.dumps(primitives))
            print(argsSQL)
            crsr.execute(argsSQL)
            crsr.commit()
        cnxn.close
        return 'injection success'
    #error handler
    except pyodbc.Error as err:
        print(err.args[1])
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
        trueID = uuid.uuid4()
        eventTrue = trueJson['true_part']
        trueSQL = "INSERT INTO [Events_True] (true_ID,event_ID) VALUES ('{}','{}')".format(trueID,eventID)
        crsr.execute(trueSQL)
        crsr.commit()
        #extract primitive and argument
        for i in range(len(eventTrue)):
            primitives = eventTrue[i].get('primitive')
            args = eventTrue[i].get('arguments')
            #inject argument
            argsSQL = "INSERT INTO [TrueArg] (true_ID,true_Arg,true_Primitive) VALUES ('{}','{}','{}')".format(trueID,json.dumps(args),json.dumps(primitives))
            print(argsSQL)
            crsr.execute(argsSQL)
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
        falseID = uuid.uuid4()
        eventFalse = falseJson['false_part']
        falseSQL = "INSERT INTO [Events_False] (false_ID,event_ID) VALUES ('{}','{}')".format(falseID,eventID)
        crsr.execute(falseSQL)
        crsr.commit()
        #extract primitive and argument
        for i in range(len(eventFalse)):
            primitives = eventFalse[i].get('primitive')
            args = eventFalse[i].get('arguments')
            #inject argument
            argsSQL = "INSERT INTO [FalseArg] (false_ID,false_Arg,false_Primitive) VALUES ('{}','{}','{}')".format(falseID,json.dumps(args),json.dumps(primitives))
            print(argsSQL)
            crsr.execute(argsSQL)
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
#this is used to test sendData
def sendDataTestrun():
    with open('event.json') as f:
        data = json.load(f)
    eventID = uuid.uuid4()
    result1 = postEvent(data,eventID)
    result3 = postTrue(data,eventID)
    result2 = postFalse(data,eventID)

    print(result1)
    print(result2)
    print(result3)