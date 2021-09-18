import mysql.connector
from mysql.connector import errorcode

def connect(username, password, databasename):
    try:
        cnx = mysql.connector.connect(host="localhost", user=username, password=password, database=databasename)
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

def main(username, password, database, stmt):
    connection = connect(username, password, database)
    cur = connection.cursor()
    cur.execute(stmt)
    myresult = cur.fetchall()
    connection.close()
    return myresult

