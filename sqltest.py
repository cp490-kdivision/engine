from config import *
#always import config like above to access Engine Connection string object

#test connection
coalEngineDBCon.ConnectionTest()
#connction info
print('Driver: ' + coalEngineDBCon.driver)
print('Server: ' +coalEngineDBCon.server)
print('DataBaseName: ' +coalEngineDBCon.database)
print('UserName: ' +coalEngineDBCon.username)
print('Password: ' +coalEngineDBCon.password)