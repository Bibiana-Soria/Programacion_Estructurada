def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("\U0001F552Oprima cualquier tecla para continuar ...\U0001F552")
  input()  

def menu_principal():
  print("\n\t\t\t \U0001F4DD.::: Sistema de Gestión de Calificaciones :::... \U0001F4DD\n\t 1️⃣ Agregar Calificación  \n\t2️⃣ Mostrar Calificación \n\t3️⃣Calcular Promedio  \n\t.4️⃣ Salir")
  opcion=input("\n\t 📚 Elige una opción (1-4): ").upper()
  return opcion

def agregar_calificaciones(lista):
  borrarPantalla()
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
  print(" \n\t\t \u2705 Acción realizada con éxito!")

def mostrar_calificaciones(lista):
  borrarPantalla()
  print(" \n\t\t\U0001F50D Mostrar Calificaciones")
  if len(lista)>0:
    print(f"{'\U0001F464Nombre':<15}{'\U0001F4DDCalif 1':<10}{'\U0001F4DDCalif 2':<10}{'\U0001F4DDCalif 3':<10}")
    print(f"{'-'*40}")
    for fila in lista:
     print(f"{fila[0]:<15}{fila[1]:<10} {fila[2]:<10}{fila[3]:<10}")
    print(f"{'-'*40}")
    cuantos=len(lista)
    print(f"Son {cuantos} alumnos")
  else:
    print("\n\t\t\u274C No hay calificaciones registradas en el sistema\u274C")
  
def calcular_promedios(lista):
  borrarPantalla()
  print("Calcular Promedio")
  if len(lista)>0:
    print(f"{'Nombre':<15}{'Promedio':<10}")
    print(f"{'-'*30}")
    promedio_grupal=0
    for fila in lista:
      nombre=fila[0]
      i=1
      suma=0
      promedio=0
      while i<=3:
        suma+=fila[i]
        i+=1
      promedio=suma/3
      print(f"{nombre:<15}{promedio:.2f}")
      promedio_grupal+=promedio
    print(f"{'-'*30}")
    promedio_grupal=promedio_grupal/len(lista)
    print(f"El promedio Grupal es: {promedio_grupal:.2f}")
  else:
    print("\n\t\t\u274C No hay calificaciones registradas en el sistema\u274C")
  


def calcular_promedios2(lista):
  borrarPantalla()
  print("\n\t\t\U0001F4DD Calcular Promedio \U0001F4DD")
  if len(lista)>0:
    print(f"{'\U0001F464 Nombre':<15}{'\U0001F4DD Promedio':<10}")
    print(f"{'-'*30}")
    promedio_grupal=0
    for fila in lista:
      nombre=fila[0]
      promedio=sum(fila[1:])/3
      print(f"{nombre:<15}{promedio:.2f}")
      promedio_grupal+=promedio
    print(f"{'-'*30}")
    promedio_grupal=promedio_grupal/len(lista)
    print(f"El promedio Grupal es: {promedio_grupal}")
  else:
     print("\n\t\t\u274CNo hay calificaciones registradas en el sistema\u274C")
  

def buscar_alumno(lista):
  borrarPantalla()
  print("Buscar Alumno")
  nombre=input("Nombre del alumno: ").upper().strip()
  if len(lista)>0:
    for fila in lista:
      if nombre==fila[0]:
        print(f"-"*50)
        print(f"{'Nombre':<15}{'Cal 1':<10}{'Cal 2':<10}{'Cal 3':<10}{'Promedio':<10}")
        print(f"-"*50)
        print(f"{nombre:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}{sum(fila[1:])/3:.2f}")
      elif nombre!=fila[0]:
       print(f"No se encontró al alumno")
    print(f"_"*40)
  else:
    print("No hay calificaciones en el sistema")

