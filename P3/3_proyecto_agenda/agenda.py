import mysql.connector 
from mysql.connector import Error
def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("\U0001F552Oprima cualquier tecla para continuar ...\U0001F552")
  input()  

def menu_principal():
  print("\n\t\t \U0001F4DD..::: Sistema de Gestión de Agenda de Contactos :::..\U0001F4DD \n\t1️⃣ Agregar contacto \n\t2️⃣ Mostrar todos los contactos \n\t3️⃣ Buscar contacto por nombre \n\t4️⃣ Modificar Contacto \n\t5️⃣ Eliminar contacto \n\t6️⃣ SALIR ")
  opcion=input("\n\t \U0001F501 Elige una opción (1-6): ")
  return opcion

def conectar():
  try:
    conexion=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="bd_agenda"
    )
    return conexion
  except Error as e:
   print(f"El error que sucedio es: {e}")
   return None

def agregar_contacto(agenda):
  borrarPantalla()
  conexionbd=conectar()
  if conexionbd!=None:
   print("\n\t\t \U0001F464Agregar Contacto \U0001F464")
   nombre=input("Nombre del contacto: ").upper().strip()
   if nombre in agenda:
     print("\n\t\t El contacto ya existe")
   else:
     tel=input("Telefono: ").strip()
     email=input("email: ").lower().strip()
     #Agregar el atributo "Nombre" al dict con los valores de tel y email en una lista
     agenda[nombre]=[tel,email]
     try:
       cursor=conexionbd.cursor()
       sql="insert into contactos (nombre, telefono,email) values (%s,%s,%s)"
       val=(nombre,tel,email)
       cursor.execute(sql,val)
       conexionbd.commit()
       print("\n\t\t\t \u2705:::LA OPERACION SE REALIZO CORRECTAMENTE \u2705:::")
     except Error as e:
        print(f"Error al intentar insertar un registro en la base de datos \n {e}")
  
def mostrar_contactos(agenda):
  borrarPantalla()
  conexionbd=conectar()
  if conexionbd!=None:
   print("\n\t\t .:: Mostrar Contactos ::.")
   cursor=conexionbd.cursor()
   sql="select * from contactos"
   cursor.execute(sql)
   registro=cursor.fetchall()
   if registro:
     print(f"{'ID':<10}{'Nombre':<20}{'Teleono':<15}{'E-mail':<15}")
     print(f"-"*60)
     for i in registro:
      print(f"{i[0]:<10}{i[1]:<20}{i[2]:<15}{i[3]:<15}")
      print(f"-"*60)
  else:
     print("\n\t\t No hay contactos en la Agenda...")
   
def buscar_contacto(agenda):
  borrarPantalla()
  conexionbd=conectar()
  if conexionbd!=None:
   print("\n\t\t \U0001F50D Buscar Contacto por Nombre \U0001F50D")
   cursor=conexionbd.cursor()
   nombre = input("Ingresa el nombre del contacto a buscar: ").upper().strip()
   sql="select * from contactos where nombre = %s"
   val=(nombre,)
   cursor.execute(sql,val)
   registro=cursor.fetchall()
   if registro:
     print(f"{'ID':<10}{'Nombre':<20}{'Teleono':<15}{'E-mail':<15}")
     (f"-"*60)
     for contacto in registro:
      print(f"{contacto[0]:<10}{contacto[1]:<20}{contacto[2]:<15}{contacto[3]:<15}")
      print(f"-"*60)
   else:
      print(f"\n\t\t El contacto '{nombre}' no se encontró en la agenda.")

def modificar_contacto(agenda):
  borrarPantalla()
  conexionbd=conectar()
  if conexionbd!=None:
   print("\n\t\t \U0001F504 Modificar Contacto \U0001F504")
   cursor=conexionbd.cursor()
   nombre = input("Ingresa el nombre del contacto a modificar: ").upper().strip()
   sql="select * from contactos where nombre = %s"
   val=(nombre,)
   cursor.execute(sql,val)
   registro=cursor.fetchall()
   if registro:
      print(f"{'ID':<10}{'Nombre':<20}{'Teleono':<15}{'E-mail':<15}")
      (f"-"*60)
      for contacto in registro:
        print(f"{contacto[0]:<10}{contacto[1]:<20}{contacto[2]:<15}{contacto[3]:<15}")
      print(f"-"*60)
      resp=input("¿Deseas modificar el contacto? (Si/No): ").upper()
      if resp=="SI":
       nuevo_nombre=input("Ingresa el nuevo nombre: ").strip().upper()
       nuevo_tel = input("Ingresa el nuevo telefono: ").strip()
       nuevo_email = input("Ingresa el nuevo email: ").lower().strip()
       sql="update contactos set nombre=%s, telefono = %s, email =%s where nombre = %s "
       val=(nuevo_nombre,nuevo_tel,nuevo_email,nombre)
       cursor.execute(sql,val)
       conexionbd.commit()
       print("\n\t\t .:: Contacto modificado con éxito ::.")
   else:
      print(f"\n\t\t El contacto {nombre} no se encontró en la agenda.")
   
def eliminar_contacto(agenda):
  borrarPantalla()
  conexionbd=conectar()
  if conexionbd!=None:
   print("\n\t\t \U0001F5D1 Eliminar Contacto \U0001F5D1")
   cursor=conexionbd.cursor()
   nombre = input("Ingresa el nombre del contacto a eliminar: ").upper().strip()
   sql="select * from contactos where nombre=%s"
   val=(nombre,)
   cursor.execute(sql,val)
   registro=cursor.fetchall()
   if registro:
     print(f"{'ID':<10}{'Nombre':<20}{'Teleono':<15}{'E-mail':<15}")
     (f"-"*60)
     for contacto in registro:
        print(f"{contacto[0]:<10}{contacto[1]:<20}{contacto[2]:<15}{contacto[3]:<15}")
     print(f"-"*60)
     resp=input(f"¿Deseas borrar el contacto de {nombre}? (Si/No): ").lower().strip()
     if resp=="si":
       sql="delete from contactos where nombre = %s "
       val=(nombre,)
       cursor.execute(sql,val)
       conexionbd.commit()
       print("\n\t\t\t \u2705:::LA OPERACION SE REALIZO CORRECTAMENTE \u2705:::")
   else: 
     print(f"\n\t\t El contacto {nombre} no se encontró en la agenda.")
   

 

