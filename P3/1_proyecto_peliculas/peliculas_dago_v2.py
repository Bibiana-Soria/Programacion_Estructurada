#Dic u objetonpara almacenar los atributos(nombre, categoria,clasificacion,genero,idioma de las peliculas)
#peliculas{
#  "nombre":"",
#  "categoria":"",
#  "clasificacion":"",
#  "genero":"",
#  "idioma":""
#}
import mysql.connector
from mysql.connector import Error
pelicula={}
def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("Oprima cualquier tecla para continuar ...")
  input()  

def conectar():
  try:
    conexion=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="bd_peliculas"
    )
    return conexion
  except Error as e:
   print(f"El error que sucedio es: {e}")
   return None
  
def crearPeliculas():
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print(" \U0001F501.:: Alta de Peliculas ::. \U0001F501 ")
    pelicula.update({"nombre":input("Ingresa el nombre: ").upper().strip()})
    pelicula.update({"categoria":input("Ingresa la categoria: ").upper().strip()})
    pelicula.update({"clasificacion":input("Ingresa la clasificacion: ").upper().strip()})
    pelicula.update({"genero":input("Ingresa el genero: ").upper().strip()})
    pelicula.update({"idioma":input("Ingresa el idioma: ").upper().strip()})

    #Agregar Registro a la base de datos 
    try:
      cursor=conexionBD.cursor()
      sql="insert into peliculas(nombre, categoria, clasificacion, genero, idioma) values(%s,%s,%s,%s,%s)"
      val=(pelicula['nombre'], pelicula['categoria'], pelicula['clasificacion'], pelicula['genero'], pelicula['idioma'])
      cursor.execute(sql,val)
      conexionBD.commit()
      print("\n\t\t\t \u2705:::LA OPERACION SE REALIZO CORRECTAMENTE \u2705:::")
    except Error as e:
      print("Error al intentar insertar un registro en la base de datos")
    
def mostrarPeliculas():
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print(".:: Consultar o Mostrar las Peliculas ::.")
    cursor=conexionBD.cursor()
    sql="select * from peliculas"
    cursor.execute(sql)
    registros=cursor.fetchall()
    if registros:
      print(f"\n\tMostrar peliculas")
      print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
      print(f"-"*80)
      for fila in registros:
        print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
      print(f"-"*80)
    else:
       print("\t \u274C.:: No hay peliculas en el Sistema ::. \u274C")

def buscarPeliculas():
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print(".:: Buscar una pelicula ::.")
    cursor=conexionBD.cursor()
    nombre=input("Dame el nombre de la pelicula a buscar: ").upper().strip()
    sql="SELECT * FROM peliculas WHERE nombre=%s"
    val=(nombre,)
    cursor.execute(sql,val)
    registros=cursor.fetchall()
    if registros:
      print(f"\n\tMostrar peliculas")
      print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
      print(f"-"*80)
      for fila in registros:
        print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
      print(f"-"*80)
    else:
       print("\t \u274C.:: La pelicula a buscar no se encuentra en el sistema ::. \u274C")

def borrarPeliculas():
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print(".:: Borrar una pelicula ::.")
    cursor=conexionBD.cursor()
    nombre=input("Dame el nombre de la pelicula a borrar: ").upper().strip()
    sql="SELECT * FROM peliculas WHERE nombre=%s"
    val=(nombre,)
    cursor.execute(sql,val)
    registros=cursor.fetchall()
    if registros:
      print(f"\n\tMostrar peliculas")
      print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
      print(f"-"*80)
      for fila in registros:
        print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
      print(f"-"*80)
      resp=input(f"¿Deseas borrar la pelicula de {nombre}? (Si/No): ").lower().strip()
      if resp=="si":
        sql="delete from peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        conexionBD.commit()
        print("\n\t\t\t \u2705:::LA OPERACION SE REALIZO CORRECTAMENTE \u2705:::")
    else:
       print("\t \u274C.:: La pelicula a borrar no se encuentra en el sistema ::. \u274C")

def modificarPeliculas():
  borrarPantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print(".:: Modificar una pelicula ::.")
    cursor=conexionBD.cursor()
    nombre=input("Dame el nombre de la pelicula a modificar: ").upper().strip()
    sql="SELECT * FROM peliculas WHERE nombre=%s"
    val=(nombre,)
    cursor.execute(sql,val)
    registros=cursor.fetchall()
    if registros:
       print(f"\n\tMostrar peliculas")
       print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
       print(f"-"*80)
       for fila in registros:
        print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
       print(f"-"*80)
       resp=input(f"¿Deseas modificar la pelicula? (Si/No): ").lower().strip()
       if resp=="si":
        pelicula["nombre"]=input("Ingresa el nombre: ").upper().strip()
        pelicula["categoria"]=input("Ingresa la categoria: ").upper().strip()
        pelicula["clasificacion"]=input("Ingresa la clasificacion: ").upper().strip()
        pelicula["genero"]=input("Ingresa el genero: ").upper().strip()
        pelicula["idioma"]=input("Ingresa el idioma: ").upper().strip()
        sql="UPDATE peliculas set nombre=%s,categoria=%s,clasificacion=%s,genero=%s,idioma=%s WHERE nombre=%s"
        val=(pelicula["nombre"],pelicula["categoria"],pelicula["clasificacion"],pelicula["genero"],pelicula["idioma"],nombre)
        cursor.execute(sql,val)
        conexionBD.commit()
        print("\n\t\t\t \u2705:::LA OPERACION SE REALIZO CORRECTAMENTE \u2705:::")
    else:
       print("\t \u274C.:: La pelicula a modificar no se encuentra en el sistema ::. \u274C")


















