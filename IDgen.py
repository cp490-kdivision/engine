import string    
import random # define the random module
import pyodbc
from config import *

def generateID(column,table,ID):
    condition=False
    while condition==False:
        S = 10  # number of characters in the string.  
        # call random.choices() string module to find the string in Uppercase + numeric data.  
        newID = ''.join(random.choices(string.ascii_lowercase + string.digits, k = S)) 
        if(ID==''):
            newID = ID + newID
        else:
            newID = ID + '-' + newID
        # check for ID on database
        #create PYOBDC connection object
        cnxn: pyodbc.Connection = pyodbc.connect(coalEngineDBCon.con)
        #cursor object from connection
        crsr: pyodbc.Cursor = cnxn.cursor()
        #select query
        select_sql = "SELECT {} FROM {} WHERE {} = '{}'".format(column,table,column,newID)
        # select_sql = "SELECT {} FROM {}".format(column,table)
        #execute select query
        crsr.execute(select_sql)
        SQLresult = crsr.fetchall()
        # Close db connetion
        cnxn.close()
        #check if ID exist
        if not SQLresult:
            condition=True
    print("The randomly generated string is : " + str(newID)) # print the random data
    return newID