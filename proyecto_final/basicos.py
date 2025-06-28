#Borrar pantalla, esperar tecla y errores

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    print("\n\t\t .: \U0001F389 OPERACION EXITOSA \U0001F389 :.")
    input("\n\t\t \U0001F550 Porfavor presione una tecla para continuar... \U0001F550")

def error():
    print("\n\t\t \u274C Esta opcion no es valida, vuelva a intentarlo... \u274C")
    input("\n\t\t \U0001F550 Presione una tecla para continuar... \U0001F550")