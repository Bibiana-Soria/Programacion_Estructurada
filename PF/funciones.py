#Borrar pantalla, esperar tecla y errores
import conexionBD
import pandas as pd


def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    print("\n\t\t .: \U0001F389 OPERACION EXITOSA \U0001F389 :.")
    input("\n\t\t \U0001F550 Porfavor presione una tecla para continuar... \U0001F550")

def error():
    print("\n\t\t \u274C Esta opcion no es valida, vuelva a intentarlo... \u274C")
    input("\n\t\t \U0001F550 Presione una tecla para continuar... \U0001F550")

def iniciarSesion():
    borrarPantalla()
    print("\n\t\t .:Inicio de Gestion de Accesorios:. \n\t\t\t 1️⃣- Iniciar Sesion \n\t\t\t 2️⃣- Nuevo User \n\t\t\t 3️⃣- Exportar datos a excel ")
    opcion=input("\n\t\t Elige una opcion (1-3): ").upper().strip()
    return opcion

def menu_principal():
    borrarPantalla()
    print("\n\t\t\t..::: \U0001F308 LAS MEZCLADITAS \U0001F308 :::... \n\t\t..::: \U0001F451 Sistema de Gestión de Accesorios \U0001F451 :::...\n\t\t\t 1️⃣- Inventario  \n\t\t\t 2️⃣- Nota de venta \n\t\t\t 3️⃣- SALIR ")
    opcion=input("\n\t\t\t \U0001F4DD una opcion (1-3): ").upper().strip()
    return opcion

def menu_inventario():
   borrarPantalla()
   print("\n\t\t\t..::: \U0001F308 LAS MEZCLADITAS \U0001F308 :::... \n\t\t..:::\U0001F45C  Sistema de Gestión de Inventario \U0001F45C :::...\n\t\t\t 1️⃣- Agregar  \n\t\t\t 2️⃣- Borrar \n\t\t\t 3️⃣- Mostrar \n\t\t\t 4️⃣- Modificar \n\t\t\t 5️⃣- Buscar ")
   respuesta=input("\n\t\t\t \U0001F4DD una opcion (1-5): ").upper().strip()
   return respuesta

def menu_venta():
   borrarPantalla()
   print("\n\t\t\t..::: \U0001F308 LAS MEZCLADITAS \U0001F308 :::... \n\t\t..:::\U0001F45C  Sistema de Gestión de Ventas \U0001F45C :::...\n\t\t\t 1️⃣- Agregar  \n\t\t\t 2️⃣- Mostrar \n\t\t\t 3️⃣- Modificar \n\t\t\t 4️⃣- Buscar \n\t\t\t 5️⃣- Borrar")
   respuesta=input("\n\t\t\t \U0001F4DD una opcion (1-5): ").upper().strip()
   return respuesta

def exportar_tablas(conexion):
    tablas = ["inventario", "ventas", "sesion"]
    excel = pd.ExcelWriter("bd_mezcladitas.xlsx")
    conexiondb=conexionBD.conexion
    for i in tablas:
        cursor=conexiondb.cursor()
        cursor.execute(f"SELECT * FROM {i}")
        columnas = [col[0] for col in cursor.description]
        datos = pd.DataFrame(cursor.fetchall(), columns=columnas)
        datos.to_excel(excel, sheet_name=i, index=False)
        cursor.close()
    excel.close()
    print("\n\t\t ✅ Tablas exportadas")