import mysql.connector
from mysql.connector import Error
def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("\U0001F552Oprima cualquier tecla para continuar ...\U0001F552")
  input()  

def conectar():
  try:
    conexion=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="bd_calificaciones"
    )
    return conexion
  except Error as e:
   print(f"El error que sucedio es: {e}")
   return None
  
def menu_principal():
  print("\n\t\t\t \U0001F4DD.::: Sistema de Gestión de Calificaciones :::... \U0001F4DD\n\t1️⃣ Agregar Calificación  \n\t2️⃣ Mostrar Calificación \n\t3️⃣ Calcular Promedio  \n\t4️⃣ Buscar Alumno \n\t 5.- Salir")
  opcion=input("\n\t 📚 Elige una opción (1-5): ").upper()
  return opcion

def agregar_calificaciones(lista):
  borrarPantalla()
  conexionbd=conectar()
  if conexionbd!=None:
   print("\n\t\t\t\U0001F4DDAgregar Calificaiones")
   nombre=input("\n\t\t \U0001F464Nombre del Alumno: ").upper().strip()
   calificaciones=[]
   for i in range(1,4):
      continua=True
      while continua:
       try:
        cal=float(input(f" \t\t\tCalificación {i}: "))
        if cal>=0 and cal<11:
         calificaciones.append(cal)
         continua=False
        else:
          print("\n\t\t \u274C Ingresa un numero válido \u274C")
       except ValueError:
        print(" \n\t\t \u274CIngresa un valor númerico \u274C") 
   lista.append([nombre]+calificaciones)
   
   try:
     cursor=conexionbd.cursor()
     sql="INSERT INTO calificaciones (nombre, calificacion1, calificacion2, calificacion3) VALUES (%s, %s, %s, %s)"
     val=(lista[0][0],calificaciones[0],calificaciones[1],calificaciones[2])
     cursor.execute(sql,val)
     conexionbd.commit() 
     print(" \n\t\t \u2705 Acción realizada con éxito!")
   except Error as e:
     print(f"Error al intentar insertar un registro en la base de datos {e}")
     
def mostrar_calificaciones(lista):
  borrarPantalla()
  conexionbd=conectar()
  if conexionbd!=None:
   print(" \n\t\t\U0001F50D Mostrar Calificaciones")
   cursor=conexionbd.cursor()
   sql="SELECT * FROM calificaciones"
   cursor.execute(sql)
   registro=cursor.fetchall()
   if registro:
     print("Mostrar calificaciones")
     print(f"{'ID':<10} {'\U0001F464Nombre':<15}{'\U0001F4DDCalif 1':<10}{'\U0001F4DDCalif 2':<10}{'\U0001F4DDCalif 3':<10}")
     print(f"-"*60)
     for alumno in registro:
       print(f"{alumno[0]:<10}{alumno[1]:<15}{alumno[2]:<15}{alumno[3]:<15}{alumno[4]}")
     print(f"-"*60)
     cuantos=len(registro)
     print(f"Son {cuantos} alumnos")
     print
  else:
     print("\n\t\t\u274C No hay calificaciones registradas en el sistema\u274C")
  
def calcular_promedios(lista):
  borrarPantalla()
  conexionbd = conectar()
  if conexionbd is not None:
   cursor=conexionbd.cursor()
   print("\n\t\t\U0001F4DD Calcular Promedio \U0001F4DD")
   print(f"{'\U0001F464 Nombre':<15}{'\U0001F4DD Promedio':<10}")
   print(f"{'-'*30}")
   sql="select * from calificaciones"
   cursor.execute(sql)
   registros=cursor.fetchall()
   if registros:
    promedio_grupal=0
    for i in registros:
     nombre=i[1]
     calificaciones=i[2:]
     promedio=sum(calificaciones)/3
     promedio_grupal+=promedio
     print(f"{nombre:<15}{promedio:.2f}")
    print(f"{'-'*30}")
    promedio_grupal=promedio_grupal/len(registros)
    print(f"El promedio Grupal es: {promedio_grupal:.2f}")

def buscar_alumno(lista):
  borrarPantalla()
  conexionbd=conectar()
  if conexionbd!=None:
   print("\n\t\t \U0001F50D Buscar Alumno \U0001F50D")
   sql="Select * from calificaciones"
   cursor=conexionbd.cursor()
   cursor.execute(sql)
   registro=cursor.fetchall()
   if registro:
     nombre=input("\U0001F464 Nombre del alumno: ").upper().strip()
     for i in registro:
       if nombre==i[1]:
        print(f"-"*50)
        print(f"{'Nombre':<15}{'Cal 1':<10}{'Cal 2':<10}{'Cal 3':<10}{'Promedio':<10}")
        print(f"-"*50)
        print(f"{i[1]:<15}{i[2]:<10}{i[3]:<10}{i[4]:<10}{sum(i[2:])/3:.2f}")
     print(f"-"*50)
   else:
     print("\u274C No hay calificaciones en el sistema \u274C")
  




    
    
  
  
  
#def calcular_promedios2(lista):
 # borrarPantalla()
 # print("\n\t\t\U0001F4DD Calcular Promedio \U0001F4DD")
  #if len(lista)>0:
 #   print(f"{'\U0001F464 Nombre':<15}{'\U0001F4DD Promedio':<10}")
 #   print(f"{'-'*30}")
 #   promedio_grupal=0
 #   for fila in lista:
 #     nombre=fila[0]
 #     promedio=sum(fila[1:])/3
 #     print(f"{nombre:<15}{promedio:.2f}")
 #     promedio_grupal+=promedio
 #   print(f"{'-'*30}")
 #   promedio_grupal=promedio_grupal/len(lista)
 #   print(f"El promedio Grupal es: {promedio_grupal}")
 # else:
 #    print("\n\t\t\u274CNo hay calificaciones registradas en el sistema\u274C")
  

    
         
 
