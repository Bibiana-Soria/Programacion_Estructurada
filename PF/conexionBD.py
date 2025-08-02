import mysql.connector
from mysql.connector import Error

try: 
  conexion=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="bd_mezcladitas"
    )
  
  cursor=conexion.cursor(buffered=True)
except Error as e:
    print(f"No se puede acceder al sistema en este momento \n\t Intentelo más tarde... ,\n\t{e}")
    