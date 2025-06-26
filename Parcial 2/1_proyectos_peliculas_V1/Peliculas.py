peliculas=[]
def agregar_pelicula():
    pelicula_a_agregar=input("¿que pelicula desea agrregar? :").upper()
    peliculas.append(pelicula_a_agregar)
    print (peliculas)

def eliminar_pelicula():
    pelicula_a_eliminar=input("¿que pelicula desea elimnar? :").upper()
    peliculas.remove(pelicula_a_eliminar)
    print(peliculas)
    print (peliculas)

def modificar_pelicula():
    pelicula_a_modificar=input("¿a que pelicula desea modifcarle el nombre? :").upper
    indice=peliculas.index(pelicula_a_modificar)
    peliculas.pop(indice)
    nuevo_nombre_de_pelicula=input("¿cual sera el nuevo nombre de la pelicula? :")
    peliculas.insert(indice, nuevo_nombre_de_pelicula)
    print (peliculas)

def consultar_pelicula():
    
    print (peliculas)

def borrar_pantalla():
    import os
    os.system("cls")

def buscar_pelicula():
    buscar_pelicula=input("¿que pelicula busca? :").upper
    for i in range(0, len(peliculas)):
        if peliculas[i]==buscar_pelicula:
            print("Si encontré la pelicula")
            numero_de_pelicula=peliculas.index(buscar_pelicula)
            print (numero_de_pelicula)
            print (peliculas)
        else:
            print("No encontré la pelicula")
        
def borrar_lista_de_peliculas():
    peliculas.clear()
    
    


def esperar_tecla():
    input=("Presione una tecla para continuar :")