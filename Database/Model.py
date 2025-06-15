#This is the file where the class of database is created 
import mysql.connector 

class Model(): 
    def __init__(self, query, values, confirmation): 
        #Make a connection to the database
        self.__connection = mysql.connector.connect(host = "localhost",
                                                   user = "administrador",
                                                   passwd = "admin123",
                                                   database = "KardexUPPE")
        self.__cursor = self.__connection.cursor()
        self.__query = query 
        self.__values = values
        self.__confirmation = confirmation

    #Command to make sql queries
    def command(self):
        self.__cursor.execute(self.__query, self.__values, self.__confirmation)
        if self.__confirmation == 1: 
            self.__connection.commit()

        result = self.__cursor.fetchall()
        self.__connection.close()
        return result 