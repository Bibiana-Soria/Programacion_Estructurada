'''crear un proyecto que permita administrar peliculas; colocar
un menu de opciones para agregar, eliminar, 
modificar y consultar peliculas
Notas:
1.- utilizar funciones y mandar llamar desde otros archivos 
2.- itilizar listas para almacenar los nombres de peliculas'''


import Peliculas
Peliculas.borrar_pantalla

def menu():
    opcion=True
    while opcion :
        seleccion=int(input("¿que accion desea hacer?(use el numero)\n\t1)agregar\n\t2)eliminar\n\t3)modificar\n\t4)consultar\n\t5)buscar pelicula\n\t6)vaciar peliculas\n\t7)salir :"))
        match seleccion:
            case int(1): 
                Peliculas.borrar_pantalla()
                print("usted esta a punnto de agregar una pelicula a la lista")
                Peliculas.esperar_tecla()
                Peliculas.agregar_pelicula()
            case int(2):
                Peliculas.borrar_pantalla()
                print("usted esta a punto de eliminar una pelicula :")
                Peliculas.esperar_tecla()
                Peliculas.eliminar_pelicula()
            case int(3):
                Peliculas.borrar_pantalla()
                print("usted esta a punto de modificar una pelicula :")
                Peliculas.esperar_tecla
                Peliculas.modificar_pelicula()
            case int(4):
                Peliculas.borrar_pantalla()
                print("usted esta a punto de consultar una pelicula :")
                Peliculas.esperar_tecla()
                Peliculas.consultar_pelicula()
            case int(5):
                Peliculas.borrar_pantalla()
                print("usted esta a punto de buscar una pelicula")
                Peliculas.esperar_tecla()
                Peliculas.buscar_pelicula()
            case int(6):
                Peliculas.borrar_pantalla()
                deseo_borrar_peliculas=input("¿usted desea borrar la lista de peliculas si/no?").upper
                if deseo_borrar_peliculas=="SI":
                    Peliculas.borrar_lista_de_peliculas()
            case int(7):
                Peliculas.borrar_pantalla()
                opcion=False

menu()