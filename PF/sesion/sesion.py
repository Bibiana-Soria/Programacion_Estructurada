from conexionBD import *

def iniciar(nombre,contrasena):
    try:
        sql="select * from sesion where nombre=%s and contrasena=%s"
        val=(nombre,contrasena)
        cursor.execute(sql,val)
        registros=cursor.fetchone()
        if registros:
            return registros
        else:
            return None
    except:
        return None

def nuevo(nombre,apellidos,email,contrasena):
    try:
        sql="insert into sesion (nombre,apellidos,email,contrasena) values(%s,%s,%s,%s)"
        val=(nombre,apellidos,email,contrasena)
        cursor.execute(sql,val)
        conexion.commit()
        return True
    except:
        return False