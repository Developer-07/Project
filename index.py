from communication import databaseCommunication
from communication import execute

print(execute.main("root", "MLemgen1709!", "php", "SELECT * FROM users WHERE id=23")[0][6])