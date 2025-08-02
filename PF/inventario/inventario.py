articulo={}
import conexionBD

def agregarInventario(categoria,nombre,marca,descripcion,precio,existencia):
 conexiondb=conexionBD.conexion
 if conexiondb!=None:
    articulo.update({"categoria":categoria})
    articulo.update({"nombre":nombre})
    articulo.update({"marca":marca})
    articulo.update({"descripcion":descripcion})
    articulo.update({"precio":precio})
    articulo.update({"existencia":existencia})
    try:
      cursor=conexiondb.cursor()
      sql="INSERT INTO inventario (categoria, nombre, marca, descripcion, precio, existencia) VALUES (%s,%s,%s,%s,%s,%s)"
      val=(articulo['categoria'], articulo['nombre'], articulo['marca'],articulo['descripcion'], articulo['precio'], articulo['existencia'])
      cursor.execute(sql,val)
      conexiondb.commit()
      return True
    except:
      print("\n\t\t Error al intentar insertar un registro en la base de datos")
      return False

def mostrarInventario():
 conexiondb=conexionBD.conexion
 if conexiondb!=None:
  try:
    cursor=conexiondb.cursor()
    sql="select * from inventario"
    cursor.execute(sql)
    return cursor.fetchall()
  except:
    return False

def modificarInventario(id_modificar,categoria,nombre,marca,descripcion,precio,existencia):
  conexiondb=conexionBD.conexion
  if conexiondb!=None:
    cursor=conexiondb.cursor()
    articulo.update({"categoria":categoria})
    articulo.update({"nombre":nombre})
    articulo.update({"marca":marca})
    articulo.update({"descripcion":descripcion})
    articulo.update({"precio":precio})
    articulo.update({"existencia":existencia})
    try:
      sql="UPDATE inventario SET categoria = %s, nombre = %s, marca = %s, descripcion = %s, precio = %s, existencia = %s WHERE id = %s"
      val=(articulo['categoria'], articulo['nombre'], articulo['marca'],articulo['descripcion'], articulo['precio'], articulo['existencia'],id_modificar)
      cursor.execute(sql,val)
      conexiondb.commit()
      return True
    except:
      print("\t \u274C.:: El articulo a modificar no se encuentra en el sistema ::. \u274C")

def buscarInventario(nombre_buscar):
  conexiondb=conexionBD.conexion
  if conexiondb!=None:
    cursor=conexiondb.cursor()
    sql=" select * from inventario where nombre = %s"
    val=(nombre_buscar,)
    cursor.execute(sql,val)
    resultados=cursor.fetchall()
    conexiondb.commit()
    return resultados
  
def borrarInventario(id_borrar):
  conexiondb = conexionBD.conexion
  if conexiondb:
      try:
          cursor = conexiondb.cursor()
          cursor.execute("SELECT COUNT(*) FROM ventas WHERE id_producto = %s", (id_borrar,))
          vinculaciones = cursor.fetchone()[0]
          if vinculaciones > 0:
              print("\n\t\t ⚠️ No se puede borrar: El producto tiene ventas asociadas.")
              return False

          cursor.execute("DELETE FROM inventario WHERE id = %s", (id_borrar,))
          conexiondb.commit()
          return True

      except Exception as err:
          print(f"\n\t\t ❌ Error al borrar: {err}")
          return False
