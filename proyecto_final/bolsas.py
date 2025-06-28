bolsas=[]

import basicos

def agregarBolsas():
    basicos.borrarPantalla()
    print("\n\t\t .:: \U0001F45C Ingreso de Nuevas Bolsas al Sistema \U0001F45C ::. ")
    nombre=input("\n\t\t \U0001F4DD nombre de la bolsa: ").upper().strip()
    marca=input("\n\t\t \U0001F4DD marca: ").upper().strip()
    descripcion=input("\n\t\t \U0001F4DD descripcion: ").upper()
    costo=input("\n\t\t \U0001F4DD costo en pesos por unidad: ").strip()
    existencia=input("\n\t\t \U0001F4DD unidades en existencia: ").strip()
    bolsas.append([nombre,marca,descripcion,costo,existencia])
    basicos.esperarTecla()

def borrarBolsa():
    basicos.borrarPantalla()
    print("\n\t\t .:: \U0001F5D1 Borrar BOLSA \U0001F5D1 ::. ")
    borrar_bolsa=input("\n\t\t \U0001F4DD nombre de la bolsa que desea borrar: ").upper().strip()
    enc=0
    for bolsa in bolsas:
        if bolsa[0]==borrar_bolsa:
            resp = input("\n\t\t \u26A0 ¿Está seguro de que quiere borrar este artículo? (S/N): ").upper().strip()
            if resp == "S":
                bolsas.remove(bolsa)
                print(f"\n\t\t \u2705 Se borró: {borrar_bolsa}")
            enc+=1
    if not enc:
        print("\n\t\t \u274C No se encontro ninguna bolsa... \u274C")
    basicos.esperarTecla()

def mostrarBolsa():
    basicos.borrarPantalla()
    print("\n\t\t .:: \U0001F50D Mostrar las Bolsas Disponibles \U0001F50D ::.")
    if len(bolsas)>0:
        print(f"\n\t\t {'Nombre':<15}{'Marca':<15}{'Descripcion':<15}{'Costo':<15}{'Existencia':<15}")
        print("\n\t\t" + "-" * 75)
        for fila in bolsas:
            print(f"\n\t\t {fila[0]:<15}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}")
        print("\n\t\t" + "-" * 75)
        num=len(bolsas)
        print(f"\n\t\t \U0001F4A1 Son en total {num} articulos")
    else:
        print("\n\t\t \u274C Lo siento, no hay articulos registrados... \u274C")
    basicos.esperarTecla()

def existenciasBolsas():
    basicos.borrarPantalla()
    print("\n\t\t .:: \u270F Modificar Existencias \u270F ::. ")
    buscar = input("\n\t\t \U0001F4DD nombre de la bolsa: ").upper().strip()
    encontro = 0
    for i in range(len(bolsas)):
        if buscar == bolsas[i][0]:
            print(f"\n\t\t Bolsa encontrada: \n\t\t - Marca: {bolsas[i][1]} \n\t\t - Descripcion: {bolsas[i][2]} \n\t\t - Costo: {bolsas[i][3]} \n\t\t - Existencia actual: {bolsas[i][4]}")
            resp = input("\n\t\t \u26A0 ¿Deseas modificar la existencia? (S/N): ").upper().strip()
            if resp == "S":
                nueva_existencia = input("\n\t\t \u2728 Nueva cantidad en existencia: ").strip()
                if nueva_existencia.isdigit():
                    bolsas[i][4] = nueva_existencia
                    encontro += 1
                    print("\n\t\t ::: \u2705 ¡Existencia actualizada con éxito! \u2705 :::")
                else:
                    print("\n\t\t \u274C ¡Valor invalido! Ingrese un numero. \u274C")
    if encontro == 0:
        print("\n\t\t \u26A0 No se encontro ninguna bolsa con ese nombre. \u26A0")
    basicos.esperarTecla()

def vaciarBolsas():
    basicos.borrarPantalla()
    print("\n\t\t .:: \u274C Borrar TODAS las bolsas del sistema \u274C ::.")
    resp=input("\n\t\t \u26A0 ¿Desea borrar todas las bolsas registradas? (S/N)").upper().strip()
    if resp=="S":
        bolsas.clear()
        print("\n\t\t \u2705 Se borraron todas las bolsas del sistema... \u2705")
        basicos.esperarTecla()