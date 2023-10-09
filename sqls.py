#un codigo de phyton para insertar un registro a la tabla empleado
import mysql.connector
from mysql.connector import Error

try:

    connection = mysql.connector.connect(host='localhost',
                                         database='prueba',
                                         user='root',
                                         password='')

    mySql_insert_query = """INSERT INTO empleado (id, nombre, apellido) 
                           VALUES 
                           (1, 'Luis', 'Garcia') """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into empleado table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into empleado table {}".format(error))
    