zapatos=[]

import basicos

def agregarZapatos():
    basicos.borrarPantalla()
    print("\n\t\t .:: \U0001F460 Ingreso de Nuevos Pares de Zapatos al Sistema \U0001F460 ::. ")
    nombre=input("\n\t\t \U0001F4DD nombre del par de zapatos: ").upper().strip()
    marca=input("\n\t\t \U0001F4DD marca: ").upper().strip()
    descripcion=input("\n\t\t \U0001F4DD descripcion: ").upper()
    costo=input("\n\t\t \U0001F4DD costo en pesos por unidad: ").strip()
    existencia=input("\n\t\t \U0001F4DD unidades en existencia: ").strip()
    zapatos.append([nombre,marca,descripcion,costo,existencia])
    basicos.esperarTecla()

def borrarZapatos():
    basicos.borrarPantalla()
    print("\n\t\t .:: \U0001F5D1 Borrar PAR DE ZAPATOS \U0001F5D1 ::. ")
    borrar_zapatos=input("\n\t\t \U0001F4DD nombre del par de zapatos que desea borrar: ").upper().strip()
    enc=0
    for zapato in zapatos:
        if zapato[0]==borrar_zapatos:
            resp = input("\n\t\t \u26A0 ¿Está seguro de que quiere borrar este artículo? (S/N): ").upper().strip()
            if resp == "S":
                zapatos.remove(zapato)
                print(f"\n\t\t \u2705 Se borró: {borrar_zapatos}")
            enc+=1
    if not enc:
        print("\n\t\t \u274C No se encontro ningun par de zapatos... \u274C")
    basicos.esperarTecla()

def mostrarZapatos():
    basicos.borrarPantalla()
    print("\n\t\t .:: \U0001F50D Mostrar los Zapatos Disponibles \U0001F50D ::.")
    if len(zapatos)>0:
        print(f"\n\t\t {'Nombre':<15}{'Marca':<15}{'Descripcion':<15}{'Costo':<15}{'Existencia':<15}")
        print("\n\t\t" + "-" * 75)
        for fila in zapatos:
            print(f"\n\t\t {fila[0]:<15}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}")
        print("\n\t\t" + "-" * 75)
        num=len(zapatos)
        print(f"\n\t\t \U0001F4A1 Son en total {num} articulos")
    else:
        print("\n\t\t \u274C Lo siento, no hay articulos registrados... \u274C")
    basicos.esperarTecla()

def existenciasZapatos():
    basicos.borrarPantalla()
    print("\n\t\t .:: \u270F Modificar Existencias \u270F ::. ")
    buscar = input("\n\t\t \U0001F4DD nombre del par de zapatos: ").upper().strip()
    encontro = 0
    for i in range(len(zapatos)):
        if buscar == zapatos[i][0]:
            print(f"\n\t\t Par de zapatos encontrado: \n\t\t - Marca: {zapatos[i][1]} \n\t\t - Descripcion: {zapatos[i][2]} \n\t\t - Costo: {zapatos[i][3]} \n\t\t - Existencia actual: {zapatos[i][4]}")
            resp = input("\n\t\t \u26A0 ¿Deseas modificar la existencia? (S/N): ").upper().strip()
            if resp == "S":
                nueva_existencia = input("\n\t\t \u2728 Nueva cantidad en existencia: ").strip()
                if nueva_existencia.isdigit():
                    zapatos[i][4] = nueva_existencia
                    encontro += 1
                    print("\n\t\t ::: \u2705 ¡Existencia actualizada con éxito! \u2705 :::")
                else:
                    print("\n\t\t \u274C ¡Valor invalido! Ingrese un numero. \u274C")
    if encontro == 0:
        print("\n\t\t \u26A0 No se encontro ningun par de zapatos con ese nombre. \u26A0")
    basicos.esperarTecla()

def vaciarZapatos():
    basicos.borrarPantalla()
    print("\n\t\t .:: \u274C Borrar TODOS los registros de zapatos del sistema \u274C ::.")
    resp=input("\n\t\t \u26A0 ¿Desea borrar todos los pares de zapatos registradas? (S/N)").upper().strip()
    if resp=="S":
        zapatos.clear()
        print("\n\t\t \u2705 Se borraron todos los pares de zapatos del sistema... \u2705")
        basicos.esperarTecla()