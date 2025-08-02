
from conexionBD import *

def agregarVenta(id_usuario,id_agregar,unidades_input):
    try:
        unidades_vendidas = int(unidades_input)
        sql = "SELECT id, nombre, categoria, precio FROM inventario WHERE id = %s"
        cursor.execute(sql, (id_agregar,))
        producto = cursor.fetchone()
        if not producto:
            print(f"\n\t\t El producto no fue encontrado en el inventario.")
            return False
        id_producto = producto[0]
        nombre = producto[1]
        categoria = producto[2]
        precio = float(producto[3])
        total = unidades_vendidas * precio
        sql_venta = "INSERT INTO ventas (id_usuario, id_producto, nombre, categoria, unidades_vendidas, total, fecha) VALUES (%s, %s, %s, %s, %s, %s, NOW())"
        datos = (id_usuario, id_producto, nombre, categoria, unidades_vendidas, total)
        cursor.execute(sql_venta, datos)
        conexion.commit()
        print(f"\n\t\t🧾 {unidades_vendidas} unidad(es) de '{nombre}' en categoría '{categoria}' por ${total:.2f}")
        sql_update = "UPDATE inventario SET existencia = existencia - %s WHERE id = %s"
        cursor.execute(sql_update, (unidades_vendidas, id_agregar))
        conexion.commit()
        return True
    except Error as e:
        print(f"\n\t\t ⚠️ Error al registrar la venta: {e}")
        return False

def modificarVenta(id_usuario,id_venta,unidades_input):
    try:
        unidades_vendidas = int(unidades_input)
        sql = "SELECT id_producto FROM ventas WHERE id = %s and id_usuario=%s"
        cursor.execute(sql, (id_venta,id_usuario))
        producto = cursor.fetchone()
        if not producto:
            print(f"\n\t\t El producto no fue encontrado en el inventario.")
            return False
        id_producto = producto[0]
        sql_producto = "SELECT nombre, categoria, precio FROM inventario WHERE id = %s"
        cursor.execute(sql_producto, (id_producto,))
        producto = cursor.fetchone()
        if not producto:
            print("\n\t\t El producto no existe en el inventario.")
            return False
        nombre, categoria, precio = producto
        total = unidades_vendidas * precio
        sql_venta = "UPDATE ventas SET unidades_vendidas=%s, total=%s where id=%s and id_usuario=%s"
        cursor.execute(sql_venta, (unidades_vendidas,total,id_venta,id_usuario))
        conexion.commit()
        print(f"\n\t\t🧾 {unidades_vendidas} unidad(es) de '{nombre}' en categoría '{categoria}' por ${total:.2f}")
        return True
    except Error as e:
        print(f"\n\t\t ⚠️ Error al registrar la venta: {e}")
        return False

def mostrarVenta(id_usuario):
    try:
        sql="select * from ventas where id_usuario=%s"
        val=(id_usuario,)
        cursor.execute(sql,val)
        conexion.commit()
        return cursor.fetchall()
    except:
        print(f"\n\t\t ⚠️ No hay ventas registradas")
        return False

def buscarVenta(id_usuario,venta_buscar):
    try:
        sql="select * from ventas where id=%s and id_usuario=%s"
        val=(venta_buscar,id_usuario)
        cursor.execute(sql,val)
        resultado=cursor.fetchall()
        conexion.commit()
        return resultado
    except:
        print(f"\n\t\t ⚠️ No hay ventas registradas")
        return False


def borrarVenta(id_borrar):
    try:
       sql="delete from ventas where id=%s"
       val=(id_borrar,)
       cursor.execute(sql,val)
    except Error as e:
       print(f"\n\t\t ⚠️ No se pudo borrar esta venta: {e}")
       return False