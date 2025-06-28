llaveros=[]

import basicos

def agregarLlaveros():
    basicos.borrarPantalla()
    print("\n\t\t .:: \U0001F511 Ingreso de Nuevos Llaveros al Sistema \U0001F511 ::. ")
    nombre=input("\n\t\t \U0001F4DD nombre del llavero: ").upper().strip()
    marca=input("\n\t\t \U0001F4DD marca: ").upper().strip()
    descripcion=input("\n\t\t \U0001F4DD descripcion: ").upper()
    costo=input("\n\t\t \U0001F4DD costo en pesos por unidad: ").strip()
    existencia=input("\n\t\t \U0001F4DD unidades en existencia: ").strip()
    llaveros.append([nombre,marca,descripcion,costo,existencia])
    basicos.esperarTecla()

def borrarLlaveros():
    basicos.borrarPantalla()
    print("\n\t\t .:: \U0001F5D1 Borrar LLAVEROS \U0001F5D1 ::. ")
    borrar_llavero=input("\n\t\t \U0001F4DD nombre del llavero que desea borrar: ").upper().strip()
    enc=0
    for llavero in llaveros:
        if llavero[0]==borrar_llavero:
            resp = input("\n\t\t \u26A0 ¿Está seguro de que quiere borrar este artículo? (S/N): ").upper().strip()
            if resp == "S":
                llaveros.remove(llavero)
                print(f"\n\t\t \u2705 Se borró: {borrar_llavero}")
            enc+=1
    if not enc:
        print("\n\t\t \u274C No se encontro ningun llavero... \u274C")
    basicos.esperarTecla()

def mostrarLlaveros():
    basicos.borrarPantalla()
    print("\n\t\t .:: \U0001F50D Mostrar los Llaveros Disponibles \U0001F50D ::.")
    if len(llaveros)>0:
        print(f"\n\t\t {'Nombre':<15}{'Marca':<15}{'Descripcion':<25}{'Costo':<15}{'Existencia':<15}")
        print("\n\t\t" + "-" * 75)
        for fila in llaveros:
            print(f"\n\t\t {fila[0]:<15}{fila[1]:<15}{fila[2]:<25}{fila[3]:<15}{fila[4]:<15}")
        print("\n\t\t" + "-" * 75)
        num=len(llaveros)
        print(f"\n\t\t \U0001F4A1 Son en total {num} articulos")
    else:
        print("\n\t\t \u274C Lo siento, no hay articulos registrados... \u274C")
    basicos.esperarTecla()

def existenciasLlaveros():
    basicos.borrarPantalla()
    print("\n\t\t .:: \u270F Modificar Existencias \u270F ::. ")
    buscar = input("\n\t\t \U0001F4DD nombre del llavero: ").upper().strip()
    encontro = 0
    for i in range(len(llaveros)):
        if buscar == llaveros[i][0]:
            print(f"\n\t\t Llavero encontrado: \n\t\t - Marca: {llaveros[i][1]} \n\t\t - Descripcion: {llaveros[i][2]} \n\t\t - Costo: {llaveros[i][3]} \n\t\t - Existencia actual: {llaveros[i][4]}")
            resp = input("\n\t\t \u26A0 ¿Deseas modificar la existencia? (S/N): ").upper().strip()
            if resp == "S":
                nueva_existencia = input("\n\t\t \u2728 Nueva cantidad en existencia: ").strip()
                if nueva_existencia.isdigit():
                    llaveros[i][4] = nueva_existencia
                    encontro += 1
                    print("\n\t\t ::: \u2705 ¡Existencia actualizada con éxito! \u2705 :::")
                else:
                    print("\n\t\t \u274C ¡Valor invalido! Ingrese un numero. \u274C")
    if encontro == 0:
        print("\n\t\t \u26A0 No se encontro ningun llavero con ese nombre. \u26A0")
    basicos.esperarTecla()

def vaciarLlaveros():
    basicos.borrarPantalla()
    print("\n\t\t .:: \u274C Borrar TODOS los llaveros del sistema \u274C ::.")
    resp=input("\n\t\t \u26A0 ¿Desea borrar todos los llaveros registradas? (S/N)").upper().strip()
    if resp=="S":
        llaveros.clear()
        print("\n\t\t \u2705 Se borraron todos los llaveros del sistema... \u2705")
        basicos.esperarTecla()