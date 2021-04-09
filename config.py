import textwrap
import pyodbc

class ConnectionString:
    def __init__(self,server,database,driver,username,password):
        self.server = server
        self.database = database
        self.driver = driver
        self.username = username
        self.password = password
        # connection string
        self.con = textwrap.dedent('''Driver={driver};Server={server};Database={database};Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'''.format(driver=driver,server=server,database=database,username=username,password=password))
    
    def ConnectionTest(self):
        try:
            #create PYOBDC connection object
            cnxn: pyodbc.Connection = pyodbc.connect(self.con)
            #cursor object from connection
            crsr: pyodbc.Cursor = cnxn.cursor()
            #select query
            select_sql = "SELECT @@version"
            #execute select query
            crsr.execute(select_sql)
            print(crsr.fetchall())
            print('datebase connection success')
            # Close db connetion
            cnxn.close()
        except:
            print("failed to conenct to database")
            cnxn.close()
        

coalEngineDBCon = ConnectionString('cp490-coal.database.windows.net','coal_engine_db','{ODBC Driver 17 for SQL Server}','user123','ketchup123$')
# # server connect info
# server = 'cp490-coal.database.windows.net'
# database = 'coal_engine_db'
# driver= '{ODBC Driver 17 for SQL Server}'