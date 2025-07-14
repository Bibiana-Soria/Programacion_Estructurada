def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("\U0001F552Oprima cualquier tecla para continuar ...\U0001F552")
  input()  

def menu_principal():
  print("\n\t\t \U0001F4DD..::: Sistema de Gestión de Agenda de Contactos :::..\U0001F4DD \n\t  1️⃣ Agregar contacto \n\t 2️⃣ Mostrar todos los contactos \n\t 3️⃣ Buscar contacto por nombre \n\t4️⃣ Modificar Contacto \n\t \n\t 5.- Eliminar contacto \n\t 6.- SALIR ")
  opcion=input("\n\t \U0001F501 Elige una opción (1-6): ")
  return opcion

def agregar_contacto(agenda):
  borrarPantalla()
  print("\n\t\t \U0001F464Agregar Contacto \U0001F464")
  nombre=input("Nombre del contacto: ").upper().strip()

  if nombre in agenda:
    print("\n\t\t El contacto ya existe")
  else:
    tel=input("Telefono: ").strip()
    email=input("email: ").lower().strip()
    #Agregar el atributo "Nombre" al dict con los valores de tel y email en una lista
    agenda[nombre]=[tel,email]
    print("\n\t\t .:: Acción realizada con exito ::.")

def mostrar_contactos(agenda):
  borrarPantalla()
  print("\n\t\t .:: Mostrar Contactos ::.")
  if not agenda:
    print("\n\t\t No hay contactos en la Agenda...")
  else:
    for nombre,datos in agenda.items():
      print(f"\n\t{'Nombre: '+ nombre}\n\t{'Telefono: ' + datos[0]}\n\t {'E-mail: '+ datos[1]}")

def buscar_contacto(agenda):
  borrarPantalla()
  print("\n\t\t \U0001F50D Buscar Contacto por Nombre \U0001F50D")
  if not agenda:
    print("\n\t\t No hay contactos para buscar en la Agenda...")
  else: 
    nombre = input("Ingresa el nombre del contacto a buscar: ").upper().strip()
    if nombre in agenda:
      datos = agenda[nombre]
      print(f"\n\t{'Nombre: ' + nombre}\n\t{'Telefono: ' + datos[0]}\n\t{'E-mail: ' + datos[1]}")
    else:
      print(f"\n\t\t El contacto '{nombre}' no se encontró en la agenda.")

def modificar_contacto(agenda):
  borrarPantalla()
  print("\n\t\t \U0001F504 Modificar Contacto \U0001F504")
  if not agenda:
    print("\n\t\t No hay contactos para modificar en la Agenda...")
  else: 
    nombre = input("Ingresa el nombre del contacto a modificar: ").upper().strip()
    if nombre in agenda:
      print(f"\n\tContacto actual: Nombre: {nombre}, Telefono: {agenda[nombre][0]}, E-mail: {agenda[nombre][1]}")
      nuevo_tel = input("Ingresa el nuevo telefono: ").strip()
      nuevo_email = input("Ingresa el nuevo email: ").lower().strip()

      if nuevo_tel:
        agenda[nombre][0] = nuevo_tel
      if nuevo_email:
        agenda[nombre][1] = nuevo_email
      print("\n\t\t .:: Contacto modificado con éxito ::.")
    else:
      print(f"\n\t\t El contacto '{nombre}' no se encontró en la agenda.")
  
def eliminar_contacto(agenda):
  borrarPantalla()
  print("\n\t\t \U0001F5D1 Eliminar Contacto \U0001F5D1")
  if not agenda:
    print("\n\t\t No hay contactos para eliminar en la Agenda...")
  else: 
    nombre = input("Ingresa el nombre del contacto a eliminar: ").upper().strip()
    if nombre in agenda:
      del agenda[nombre]
      print(f"\n\t\t .:: Contacto '{nombre}' eliminado con éxito ::.")
    else:
      print(f"\n\t\t El contacto '{nombre}' no se encontró en la agenda.")

