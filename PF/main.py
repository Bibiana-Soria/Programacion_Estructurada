#Sistema en consola para la administracion de diversos accesorios usando diccionarios y funciones
from conexionBD import *
import funciones
from sesion import sesion
from inventario import inventario
from nota_venta import venta
import getpass

def main():
   opcion=True
   while opcion:
      try:
         funciones.borrarPantalla()
         opcion=funciones.iniciarSesion()

         if opcion=="1":
            funciones.borrarPantalla()
            print("\n\t\t .:: Nueva Sesion ::.")
            nombre=input("\n\t\t Ingresa tu usuario registrado: ").upper().strip()
            contrasena=getpass.getpass("\n\t\t Ingresa tu contraseña: ").strip()
            registro=sesion.iniciar(nombre,contrasena)
            if registro:
               menuPrincipal(registro[0],registro[1],registro[2])
            else:
               print("\n\t\t Usuario y/o contraseña incorrectos...")
               funciones.esperarTecla()
         elif opcion=="2":
               funciones.borrarPantalla()
               print("\n\t\t .: Nuevo Usuario :.")
               nombre=input("\n\t\t Nombre: ").upper().strip()
               apellidos=input("\n\t\t Apellidos: ").upper().strip()
               email=input("\n\t\t Email: ").lower().strip()
               contrasena=getpass.getpass("\n\t\t Contraseña: ").strip()
               result=sesion.nuevo(nombre,apellidos,email,contrasena)
               if result:
                  print(f"\n\t\t {nombre} registrado correctamente...")
               else:
                  print("\n\t\t ...Sucedio algo inesperado. Intente de nuevo...")
               funciones.esperarTecla()
         elif opcion=="3":
            guardar=input("\n\t\t Desea exportar los datos a Excel? (si/no): ").lower().strip()
            if guardar=="si":
               funciones.exportar_tablas(conexion)   
            else:
               print("\n\t\t Gracias...")
            print("\n\t\t Saliendo...")
            opcion=False
            funciones.esperarTecla()
         else:
            funciones.error()
      except Exception as e:
         print(f"\n\t\t Ha ocurrido un error inesperado: {e}")
         funciones.esperarTecla()


def menuPrincipal(id_usuario,nombre,apellidos):
   while True:
      funciones.borrarPantalla()
      print(f"\n\t\t ...Bienvenido {nombre} {apellidos}...")
      input("\n\t\t Por favor, presiona una tecla para continuar...")
      opcion=funciones.menu_principal()
      if opcion=="1":
         funciones.borrarPantalla()
         inven=funciones.menu_inventario()
         if inven=="1":
            try:
               funciones.borrarPantalla()
               print("\n\t\t \U0001F4DD ..:: Agregar Inventario ::.. \U0001F4DD")
               categoria=input("\n\t\t \U0001F4DD Categoria: ").upper().strip()
               nombre=input("\n\t\t \U0001F4DD Nombre: ").upper().strip()
               marca=input("\n\t\t \U0001F4DD Marca: ").upper().strip()
               descripcion=input("\n\t\t \U0001F4DD Descripción: ").upper().strip()
               precio=input("\n\t\t \U0001F4DD Precio: ").upper().strip()
               existencia=input("\n\t\t \U0001F4DD Unidades en existencia: ").upper().strip()
               resp_ingresar=inventario.agregarInventario(categoria,nombre,marca,descripcion,precio,existencia)
               if resp_ingresar:
                  print("\n\t\t Articulo agregado exitosamente...")
            except:
               print("\n\t\t ...Ocurrio algo innesperado, vuelve a intentarlo...")
            funciones.esperarTecla()
         elif inven=="2":
            try:
               funciones.borrarPantalla()
               print("\n\t\t \u26A0 ..:: Borrar Inventario ::.. \u26A0")
               borrar=inventario.mostrarInventario()
               if borrar:
                  print(f"{'ID':<10} {'Categoria':<15} {'Nombre':<15} {'Marca':<15} {'Descripción':<20} {'Precio':<15} {'Existencia':<15}")
                  print(f"-"*120)
                  for fila in borrar:
                     print(f"{fila[0]:<10} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15} {fila[4]:<20} {fila[5]:<15} {fila[6]}")
                  print(f"-"*120)
               else:
                  print("\t \u274C.:: No hay Articulos en el Sistema ::. \u274C")
               id_borrar=input("\U0001F4DD Ingresa el id del articulo a borrar: ").strip()
               resp=input("¿Deseas eliminar el articulo del inventario? (Si/No)?: ").lower()
               if resp=="si":
                  respuesta=inventario.borrarInventario(id_borrar)
                  if respuesta:
                     print("\n\t\t Se borró exitosamente")
               if resp=="no":
                  funciones.esperarTecla()
            except:
               print("\n\t\t ...Ocurrio algo innesperado, vuelve a intentarlo...")
            funciones.esperarTecla()
         elif inven=="3":
            try:
               funciones.borrarPantalla()
               print("\n\t\t \U0001F4C2 ..:: Mostrar Inventario ::.. \U0001F4C2")
               mostrar=inventario.mostrarInventario()
               if mostrar:
                  print(f"{'ID':<10} {'Categoria':<15} {'Nombre':<15} {'Marca':<15} {'Descripción':<20} {'Precio':<15} {'Existencia':<15}")
                  print(f"-"*120)
                  for fila in mostrar:
                     print(f"{fila[0]:<10} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15} {fila[4]:<20} {fila[5]:<15} {fila[6]}")
                  print(f"-"*120)
               else:
                  print("\t \u274C.:: No hay Articulos en el Sistema ::. \u274C")
            except:
               print("\n\t\t ...Ocurrio algo innesperado, vuelve a intentarlo...")
            funciones.esperarTecla()
         elif inven=="4":
            try:
               funciones.borrarPantalla()
               print ("\n\t\t \U0001F501 ..:: Modificar Inventario ::.. \U0001F501")
               modif=inventario.mostrarInventario()
               if modif:
                  print(f"{'ID':<10} {'Cartegoria':<15} {'Nombre':<15} {'Marca':<15} {'Descripción':<20} {'Precio':<15} {'Existencia':<15}")
                  print(f"-"*120)
                  for fila in modif:
                     print(f"{fila[0]:<10} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15} {fila[4]:<20} {fila[5]:<15} {fila[6]}")
                  print(f"-"*120)
               else:
                  print("\t \u274C.:: No hay Articulos en el Sistema ::. \u274C")
               pregunta_modificar=input("¿Deseas modificar un articulo del inventario? (Si/No)?: ").lower()
               if pregunta_modificar=="si":
                  id_modificar=input("\U0001F50D Ingresa el id del articulo: ").strip()
                  categoria=input("\n\t\t \U0001F4DD Categoria: ").upper().strip()
                  nombre=input("\n\t\t \U0001F4DD Nombre: ").upper().strip()
                  marca=input("\n\t\t \U0001F4DD Marca: ").upper().strip()
                  descripcion=input("\n\t\t \U0001F4DD Descripción: ").upper().strip()
                  precio=input("\n\t\t \U0001F4DD Precio: ").strip()
                  existencia=input("\n\t\t \U0001F4DD Unidades en existencia: ").strip()
                  respuesta_modificar=inventario.modificarInventario(id_modificar,categoria,nombre,marca,descripcion,precio,existencia)
                  if respuesta_modificar:
                     print("\n\t\t El articulo se modifico correctamente...")
            except:
               print("\n\t\t ...Ocurrio algo innesperado, vuelve a intentarlo...")
            funciones.esperarTecla()
         elif inven=="5":
            try:
               funciones.borrarPantalla()
               print("\n\t\t \U0001F50D ..:: Buscar un Artículo ::.. \U0001F50D")
               nombre_buscar=input("\U0001F50D Ingresa el nombre del articulo: ").upper().strip()
               busc=inventario.buscarInventario(nombre_buscar)
               if busc:
                  print(f"{'ID':<10} {'Tipo':<15} {'Nombre':<15} {'Marca':<15} {'Descripción':<20} {'Precio':<15} {'Existencia':<15}")
                  print(f"-"*120)
                  for fila in busc:
                     print(f"{fila[0]:<10} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15} {fila[4]:<20} {fila[5]:<15} {fila[6]}")
                  print(f"-"*120)
            except:
               print("\n\t\t ...Ocurrio algo innesperado, vuelve a intentarlo...")
            funciones.esperarTecla()
         else:
            funciones.error()
      if opcion=="2":
         funciones.borrarPantalla()
         vent=funciones.menu_venta()
         if vent=="1":
            try:
               funciones.borrarPantalla()
               print("\n\t\t \U0001F4DB ..:: Agregar Nueva Venta ::.. \U0001F4DB")
               nueva_vent=inventario.mostrarInventario()
               if nueva_vent:
                  print(f"{'ID':<10} {'Categoria':<15} {'Nombre':<15} {'Marca':<15} {'Descripción':<20} {'Precio':<15} {'Existencia':<15}")
                  print(f"-"*120)
                  for fila in nueva_vent:
                     print(f"{fila[0]:<10} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15} {fila[4]:<20} {fila[5]:<15} {fila[6]}")
                  print(f"-"*120)
               else:
                  print("\t \u274C.:: No hay Articulos en el Sistema ::. \u274C")
               id_agregar = input("\n\t\t ID del producto: ").upper().strip()
               unidades_input = input("\n\t\t Unidades vendidas: ").strip()
               nueva=venta.agregarVenta(id_usuario,id_agregar,unidades_input)
               if nueva:
                  print("\n\t\t Venta agregada exitosamente...")
            except:
               print("\n\t\t ...Ocurrio algo innesperado, vuelve a intentarlo...")
            funciones.esperarTecla()
         elif vent=="2":
            try:
               funciones.borrarPantalla()
               print("\n\t\t \U0001F4C2 ..:: Mostrar Ventas ::.. \U0001F4C2")
               mostrar_vent=venta.mostrarVenta(id_usuario)
               if mostrar_vent:
                  print(f"{'ID_venta':<10}{'ID_user':<10}{'ID_producto':<15}{'nombre':<15}{'categoria':<15}{'unidades_vendidas':<23}{'total':<25}{'fecha':<15}")
                  print(f"-"*130)
                  for fila in mostrar_vent:
                     print(f"{fila[0]:<10}{fila[1]:<10}{fila[2]:<15}{fila[3]:<15}{fila[4]:<20}{fila[5]:<20}{fila[6]:<25}{fila[7]}")
                  print(f"-"*130)
            except:
               print("\n\t\t ...Ocurrio algo innesperado, vuelve a intentarlo...")
            funciones.esperarTecla()
         elif vent=="3":
            try:
               funciones.borrarPantalla()
               print ("\n\t\t \U0001F501 ..:: Modificar Ventas ::.. \U0001F501")
               modif_venta=venta.mostrarVenta(id_usuario)
               if modif_venta:
                  print(f"{'ID_venta':<10}{'ID_user':<10}{'ID_producto':<15}{'nombre':<15}{'categoria':<15}{'unidades_vendidas':<23}{'total':<25}{'fecha':<15}")
                  print(f"-"*130)
                  for fila in modif_venta:
                     print(f"{fila[0]:<10}{fila[1]:<10}{fila[2]:<15}{fila[3]:<15}{fila[4]:<20}{fila[5]:<20}{fila[6]:<25}{fila[7]}")
                  print(f"-"*130)
               else:
                  print("\t \u274C.:: No hay Articulos en el Sistema ::. \u274C")
               preg_modificar=input("¿Deseas modificar un articulo del alguna venta? (Si/No)?: ").lower()
               if preg_modificar=="si":
                  id_venta = input("\n\t\t ID de venta a modificar: ").strip()
                  unidades_input = input("\n\t\t Unidades vendidas: ").strip()
                  modificar_venta=venta.modificarVenta(id_usuario,id_venta,unidades_input)
                  if modificar_venta:
                     print("\n\t\t La venta se modifico exitosamente...")
            except:
               print("\n\t\t ...Ocurrio algo innesperado, vuelve a intentarlo...")
            funciones.esperarTecla()
         elif vent=="4":
            try:
               funciones.borrarPantalla()
               print("\n\t\t \U0001F50D ..:: Buscar Venta ::.. \U0001F50D")
               buscar_venta=input("\n\t\t ID de venta a buscar: ").strip()
               buscar=venta.buscarVenta(id_usuario,buscar_venta)
               if buscar:
                  print(f"{'ID_venta':<10}{'ID_user':<10}{'ID_producto':<15}{'nombre':<15}{'categoria':<15}{'unidades_vendidas':<23}{'total':<25}{'fecha':<15}")
                  print(f"-"*130)
                  for fila in buscar:
                     print(f"{fila[0]:<10}{fila[1]:<10}{fila[2]:<15}{fila[3]:<15}{fila[4]:<20}{fila[5]:<20}{fila[6]:<25}{fila[7]}")
                  print(f"-"*130)
               else:
                  print("\t \u274C.:: No hay Articulos en el Sistema ::. \u274C")
            except:
               print("\n\t\t ...Ocurrio algo innesperado, vuelve a intentarlo...")
            funciones.esperarTecla()
         elif vent=="5":
            try:
               funciones.borrarPantalla()
               print("\n\t\t \U0001F50D ..:: Borrar Venta ::.. \U0001F50D")
               eliminar=venta.mostrarVenta(id_usuario)
               if eliminar:
                  print(f"{'ID_venta':<10}{'ID_user':<10}{'ID_producto':<15}{'nombre':<15}{'categoria':<15}{'unidades_vendidas':<23}{'total':<25}{'fecha':<15}")
                  print(f"-"*130)
                  for fila in eliminar:
                     print(f"{fila[0]:<10}{fila[1]:<10}{fila[2]:<15}{fila[3]:<15}{fila[4]:<20}{fila[5]:<20}{fila[6]:<25}{fila[7]}")
                  print(f"-"*130)
                  id_eliminar=input("\n\t\t ID de venta a eliminar: ").strip()
                  preg_eliminar=input("\n\t\t ¿Desea eliminar la venta? (si/no): ").lower()
                  if preg_eliminar=="si":
                     borrar_venta=venta.borrarVenta(id_eliminar)
                     if borrar_venta:
                        print("\n\t\t Se borro la venta...")
                  if preg_eliminar=="no":
                     funciones.esperarTecla()
               else:
                  print("\t \u274C.:: No hay Articulos en el Sistema ::. \u274C")
               
            except:
               print("\n\t\t ...Ocurrio algo innesperado, vuelve a intentarlo...")
            funciones.esperarTecla()
         else:
            funciones.error()
      if opcion=="3":
         break

if __name__=="__main__":
    main()
