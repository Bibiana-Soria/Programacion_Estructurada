#proyecto 1 
# Crear un proyecto que permita Gestionar (Administrar) peliculas, colocar un menu de opciones para agregar, eliminar, modificar y consultar peliculas. 

#Notas: 
# 1.- Utilizar funciones y mandar llamar desde otro archivo
# 2.- Utilizar dict para almacenar los siguientes atributos: (nombre, categoria,clasificacion,genero,idioma) de las peliculas#
# 3.- Utilizar e implementar una BD para gestionar las peliculas
#  

import peliculas_dago_v2

opcion=True
while opcion:
    peliculas_dago_v2.borrarPantalla()
    print("\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t\t 1.- Crear  \n\t\t\t 2.- Borrar \n\t\t\t 3.- Mostrar \n\t\t\t 4.- Modificar  \n\t\t\t 5.- Buscar \n\t\t\t 6.- Salir")
    opcion=input("\n\t\t\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas_dago_v2.crearPeliculas()
            peliculas_dago_v2.esperarTecla()
        case "2":
            peliculas_dago_v2.borrarPeliculas()
            peliculas_dago_v2.esperarTecla()
        case "3":
            peliculas_dago_v2.mostrarPeliculas()
            peliculas_dago_v2.esperarTecla() 
        case "4":
            peliculas_dago_v2.modificarPeliculas()
            peliculas_dago_v2.esperarTecla()
        case "5":
            peliculas_dago_v2.buscarPeliculas()
            peliculas_dago_v2.esperarTecla()
        case "6":
            opcion=False    
            peliculas_dago_v2.borrarPantalla()
            print("\n\tTerminaste la ejecucion del SW")    
        case _:
            peliculas_dago_v2.borrarPantalla()
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")