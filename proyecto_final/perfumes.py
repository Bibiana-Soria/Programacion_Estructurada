perfumes=[]

import basicos

def agregarPerfumes():
    basicos.borrarPantalla()
    print("\n\t\t .:: \U0001F490 Ingreso de Nuevos Perfumes al Sistema \U0001F490 ::. ")
    nombre=input("\n\t\t \U0001F4DD nombre del perfume: ").upper().strip()
    marca=input("\n\t\t \U0001F4DD marca: ").upper().strip()
    descripcion=input("\n\t\t \U0001F4DD descripcion: ").upper()
    costo=input("\n\t\t \U0001F4DD costo en pesos por unidad: ").strip()
    existencia=input("\n\t\t \U0001F4DD unidades en existencia: ").strip()
    perfumes.append([nombre,marca,descripcion,costo,existencia])
    basicos.esperarTecla()

def borrarPerfumes():
    basicos.borrarPantalla()
    print("\n\t\t .:: \U0001F5D1 Borrar PERFUMES \U0001F5D1 ::. ")
    borrar_perfume=input("\n\t\t \U0001F4DD nombre del perfume que desea borrar: ").upper().strip()
    enc=0
    for perfume in perfumes:
        if perfume[0]==borrar_perfume:
            resp = input("\n\t\t \u26A0 ¿Está seguro de que quiere borrar este artículo? (S/N): ").upper().strip()
            if resp == "S":
                perfumes.remove(perfume)
                print(f"\n\t\t \u2705 Se borró: {borrar_perfume}")
            enc+=1
    if not enc:
        print("\n\t\t \u274C No se encontro ningun perfume... \u274C")
    basicos.esperarTecla()

def mostrarPerfumes():
    basicos.borrarPantalla()
    print("\n\t\t .:: \U0001F50D Mostrar los Perfumes Disponibles \U0001F50D ::.")
    if len(perfumes)>0:
        print(f"\n\t\t {'Nombre':<15}{'Marca':<15}{'Descripcion':<15}{'Costo':<15}{'Existencia':<15}")
        print("\n\t\t" + "-" * 75)
        for fila in perfumes:
            print(f"\n\t\t {fila[0]:<15}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}")
        print("\n\t\t" + "-" * 75)
        num=len(perfumes)
        print(f"\n\t\t \U0001F4A1 Son en total {num} articulos")
    else:
        print("\n\t\t \u274C Lo siento, no hay articulos registrados... \u274C")
    basicos.esperarTecla()

def existenciasPerfumes():
    basicos.borrarPantalla()
    print("\n\t\t .:: \u270F Modificar Existencias \u270F ::. ")
    buscar = input("\n\t\t \U0001F4DD nombre del perfume: ").upper().strip()
    encontro = 0
    for i in range(len(perfumes)):
        if buscar == perfumes[i][0]:
            print(f"\n\t\t Perfume encontrado: \n\t\t - Marca: {perfumes[i][1]} \n\t\t - Descripcion: {perfumes[i][2]} \n\t\t - Costo: {perfumes[i][3]} \n\t\t - Existencia actual: {perfumes[i][4]}")
            resp = input("\n\t\t \u26A0 ¿Deseas modificar la existencia? (S/N): ").upper().strip()
            if resp == "S":
                nueva_existencia = input("\n\t\t \u2728 Nueva cantidad en existencia: ").strip()
                if nueva_existencia.isdigit():
                    perfumes[i][4] = nueva_existencia
                    encontro += 1
                    print("\n\t\t ::: \u2705 ¡Existencia actualizada con éxito! \u2705 :::")
                else:
                    print("\n\t\t \u274C ¡Valor invalido! Ingrese un numero. \u274C")
    if encontro == 0:
        print("\n\t\t \u26A0 No se encontro ningun perfume con ese nombre. \u26A0")
    basicos.esperarTecla()

def vaciarPerfumes():
    basicos.borrarPantalla()
    print("\n\t\t .:: \u274C Borrar TODOS los perfumes del sistema \u274C ::.")
    resp=input("\n\t\t \u26A0 ¿Desea borrar todos los perfumes registradas? (S/N)").upper().strip()
    if resp=="S":
        perfumes.clear()
        print("\n\t\t \u2705 Se borraron todos los perfumes del sistema... \u2705")
        basicos.esperarTecla()