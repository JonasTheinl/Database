import sqlite3
from urllib.request import pathname2url

#Class to work with simple Database commands
class DatabaseManagement:
    
    #Connect to a database
    def connectToDatabase(self, db):
        conn = sqlite3.connect(db)
        return conn
    
    #Close connection to a database
    def closeDatabaseConnection(self, conn):
        conn.close()
        
    #Create a database table
    def createDatabaseTable(self, conn, sql):
        cursor = conn.cursor()
        cursor.execute(sql)
        
    #Insert data in a database with a tuple
    def insertIntoDatabaseTable(self, conn, sql, data_tuple):
        cursor = conn.cursor()
        cursor.execute(sql, data_tuple)
        conn.commit()
        
    #Check if a database exists
    def checkIfDatabaseExist(self, db):
        try:
            dburi = 'file:{}?mode=rw'.format(pathname2url(db))
            conn = sqlite3.connect(dburi, uri=True)
            conn.close()
            return True
        except sqlite3.OperationalError:
            return False