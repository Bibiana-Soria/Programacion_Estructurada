'''
Proyecto 3.
Crear un proyecto que permita Gestionar (Administrar) Califiaciones colocar un menu de opciones para agregar, mostrar, calcular promedio calificaciones de un estidiante

Notas: 
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar listas para almacenar los nombres y calificaciones

'''

import calificaciones
def main():
    datos=[]
    opcion=True
    while opcion:
        calificaciones.borrarPantalla()
        opcion=calificaciones.menu_principal()
    
        match opcion:
            case "1":
             calificaciones.agregar_calificaciones(datos)
             calificaciones.esperarTecla()
            case "2":
             calificaciones.mostrar_calificaciones(datos)
             calificaciones.esperarTecla()
            case "3":
             calificaciones.calcular_promedios(datos)
             calificaciones.esperarTecla()
            case "4":
             calificaciones.buscar_alumno(datos)
             calificaciones.esperarTecla()
            case "5":
             opcion=False
             calificaciones.borrarPantalla()
             print("..::Terminaste la ejecucion del SW::..")
            case _:
              opcion=True
              input("\n\tOpción invalida vuelva a intentarlo ... por favor")
              calificaciones.esperarTecla()


if __name__=="__main__":
  main()