#Dic u objetonpara almacenar los atributos(nombre, categoria,clasificacion,genero,idioma de las peliculas)
#peliculas{
#  "nombre":"",
#  "categoria":"",
#  "clasificacion":"",
#  "genero":"",
#  "idioma":""
#}

pelicula={}
def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("Oprima cualquier tecla para continuar ...")
  input()  

def crearPeliculas():
  borrarPantalla()
  print(" \U0001F501.:: Alta de Peliculas ::. \U0001F501 ")
  pelicula.update({"nombre":input("Ingresa el nombre: ").upper().strip()})
  pelicula.update({"categoria":input("Ingresa la categoria: ").upper().strip()})
  pelicula.update({"clasificacion":input("Ingresa la clasificacion: ").upper().strip()})
  pelicula.update({"genero":input("Ingresa el genero: ").upper().strip()})
  pelicula.update({"idioma":input("Ingresa el idioma: ").upper().strip()})
  print("\n\t\t\t \u2705:::LA OPERACION SE REALIZO CORRECTAMENTE \u2705:::")
  esperarTecla()

def mostrarPeliculas():
  borrarPantalla()
  print(".:: Consultar o Mostrar las Peliculas ::.")
  if len(pelicula)>0:
    for i in pelicula:
      print(f"{(i)}:{pelicula[i]}")
  else:
    print("\t \u274C.:: No hay peliculas en el Sistema ::. \u274C")

def borrarPeliculas():
  borrarPantalla()
  print("\n\t.:: Borrar o quitar TODAS las peliculas ::.")
  resp=input("¿Deseas quitar o borrar todas las peliculas del sistema? (Si/No)").lower()
  if resp=="si":
    pelicula.clear()
    print("\n\t\t\t :::LA OPERACION SE REALIZO CORRECTAMENTE:::")

def agregarCaracteristicaPeliculas():
  borrarPantalla()
  print("\n\t.:: Agregar Caracteristica a Peliculas ::.")
  atributo=input("Ingresa la nueva caracteristica de la peliculas: ").lower().strip()
  valor=input("El valor de la caracteristica de la pelicula: ").upper().strip()
  pelicula.update({atributo:valor})
  print("\n\t\t\t :::LA OPERACION SE REALIZO CORRECTAMENTE:::")

def modificarCaracteristicaPeliculas():
  borrarPantalla()
  print("\n\t.:: Modificar Caracteristicas de Peliculas ::.")
  if len(pelicula)>0:
    print(f"\n\tValor actual: \n ")
    for i in pelicula:
      print(f"\t{(i)}: {pelicula[i]}")
      resp=input(f"\¿Deseas cambiar el valor de {i}? (Si/No) ").lower()
      if resp=="si":
        pelicula.update({f"{i}": input("\t \U0001F501 el nuevo valor: ").upper().strip()})
        print("\n\t\t:::\u2705 ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO \u2705::: ")
        esperarTecla()
        borrarPantalla()
  else:
    print("\t..:: \u26A0 No hay peliculas en el sistema \u26A0 ::..")
    esperarTecla()


def borrarCaracteristicaPeliculas():
  borrarPantalla()
  print("\n\t \U0001F4DB.:: Borrar Caracteristica de una Pelicula ::. \U0001F4DB \n")
  if len(pelicula)>0:
    print(f"\n\t Valor actual: \n")
    for i in pelicula:
      print(f"\t{(i)}: {pelicula[i]}")
    resp=input(f"\¿Deseas borrar una caracyerística? (Si/No)").lower()
    if resp=="si":
      atributo=input("Escribe la caracteristica que deseas borrar o quitar: ")
      pelicula.pop(atributo)
      print("\n\t\t:::\u2705 ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO\ u2705::: \u26A0 ")
      esperarTecla()
      borrarPantalla()
  else:
    print("\t..:: \u26A0 No hay peliculas en el sistema \u26A0 ::..")
    esperarTecla()
    




