import funciones
from usuarios import usuario
from notas import nota
import getpass

def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_usurios()

        if opcion=="1" or opcion=="REGISTRO":
            funciones.borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
            apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
            email=input("\t Ingresa tu email: ").lower().strip()
            #password=input("\t Ingresa tu contraseña: ").strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo
            resultado=usuario.registrar(nombre,apellidos,email,password)
            if resultado:
                print(f"\n\t {nombre} {apellidos}, se registro correctamente con el email: {email}")
            else: 
                print(f"\n\t ...Por favor intentelo de nuevo, no fue posible registrar al usuario")
            funciones.esperarTecla()
        elif opcion=="2" or opcion=="LOGIN": 
            funciones.borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ").lower().strip()
            #password=input("\t Ingresa tu contraseña: ").strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo 
            registro=usuario.iniciar_sesion(email,password)
            if registro:
             menu_notas(registro[0],registro[1],registro[2])
            else:
                print(f"\n\t E-mail y/o contraseña incorrectos, vuelva a intentarlo...")
                funciones.esperarTecla()
              
        elif opcion=="3" or opcion=="SALIR": 
            print("Termino la Ejecución del Sistema")
            opcion=False
            funciones.esperarTecla()  
        else:
            print("Opcion no valida")
            opcion=True
            funciones.esperarTecla() 

def menu_notas(usuario_id,nombre,apellidos):
    while True:
        funciones.borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        opcion=funciones.menu_notas()

        if opcion == '1' or opcion=="CREAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo=input("\tTitulo: ")
            descripcion=input("\tDescripción: ")
            #Agregar codigo
            respuesta=nota.crear(usuario_id, titulo, descripcion)
            if respuesta:
                print(f"\t\tSe creo la nota: {titulo} exitosamente")
            else:
                print(f"No fue posible crear la nota en este momento, vuelve a intentar...")
            funciones.esperarTecla()    
        elif opcion == '2' or opcion=="MOSTRAR":
            funciones.borrarPantalla()
            #Agregar codigo  
            lista_notas=nota.mostrar(usuario_id)
            if lista_notas:
             print(f"\n\tMostrar notas")
             print(f"{'ID':<10}{'titulo':<15}{'descripcion':<15}{'fecha':<15}")
             print(f"-"*80)
             for fila in lista_notas:
              print(f"{fila[0]:<10}{fila[2]:<15}{fila[3]:<15}{fila[4]}")
             print(f"-"*80)
            else:
                print("\n\t No existen noas de acuerdo al usuario")
            funciones.esperarTecla()
        elif opcion == '3' or opcion=="CAMBIAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar un Nota ::. \n")
            notas=nota.mostrar(usuario_id)
            if notas:
             print(f"\n\tMostrar notas")
             print(f"{'ID':<10}{'titulo':<15}{'descripcion':<15}{'fecha':<15}")
             print(f"-"*80)
             for fila in notas:
              print(f"{fila[0]:<10}{fila[2]:<15}{fila[3]:<15}{fila[4]}")
             print(f"-"*80)
            else:
                print("\n\t No existen notas de acuerdo al usuario")
            resp=input("¿Deseas cambiar la nota?: ").upper()
            if resp=="SI":
             id = input("\t \t ID de la nota a actualizar: ")
             titulo = input("\t Nuevo título: ")
             descripcion = input("\t Nueva descripción: ")
             #Agregar codigo
             respuesta=nota.cambiar(id, titulo, descripcion)
             if respuesta:
                print(f"\n\t\t Se actualizo la nota: {titulo} exitosamente")
             else:
                print(f"\n\t\t no fue posible actualizar la nota en este momento...")
            funciones.esperarTecla()      
        elif opcion == '4' or opcion=="ELIMINAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar un Nota ::. \n")
            notas=nota.mostrar(usuario_id)
            if notas:
             print(f"\n\tMostrar notas")
             print(f"{'ID':<10}{'titulo':<15}{'descripcion':<15}{'fecha':<15}")
             print(f"-"*80)
             for fila in notas:
              print(f"{fila[0]:<10}{fila[2]:<15}{fila[3]:<15}{fila[4]}")
             print(f"-"*80)
            else:
             print("\n\t No existen notas de acuerdo al usuario")
            resp=input("¿Deseas cambiar la nota?: ").upper()
            if resp=="SI":
             id = input("\t \t ID de la nota a eliminar: ")
             #Agregar codigo
             respuesta=nota.borrar(id)
             if respuesta:
                print(f"\n\t\tSe borró la nota exitosamente")
             else:
                print("\n\t\t No fue posible borrar la nota")
            funciones.esperarTecla()    
        elif opcion == '5' or opcion=="SALIR":
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()    


