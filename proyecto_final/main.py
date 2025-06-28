#Sistema en consola para la administracion de diversos accesorios usando listas y funciones
import bolsas,basicos,zapatos,perfumes,llaveros

opcion=True


while opcion:
    basicos.borrarPantalla()
    print("\n\t\t\t..::: \U0001F308 LAS MEZCLADITAS \U0001F308 :::... \n\t\t..::: \U0001F451 Sistema de Gestión de Accesorios \U0001F451 :::...\n\t\t\t 1️⃣- Bolsas  \n\t\t\t 2️⃣- Zapatos \n\t\t\t 3️⃣- Perfumes \n\t\t\t 4️⃣- LLaveros \n\t\t\t 5️⃣- SALIR ")
    opcion=input("\n\t\t\t \U0001F4DD una opcion (1-5): ").upper().strip()

    match opcion:
        case "1":
            basicos.borrarPantalla()
            print("\n\t\t\t..::: \U0001F308 LAS MEZCLADITAS \U0001F308 :::... \n\t\t..:::\U0001F45C  Sistema de Gestión de Bolsas \U0001F45C :::...\n\t\t\t 1️⃣- Agregar  \n\t\t\t 2️⃣- Borrar \n\t\t\t 3️⃣- Mostrar \n\t\t\t 4️⃣- Modificar \n\t\t\t 5️⃣- Vaciar")
            bolsasOpc=input("\n\t\t\t \U0001F4DD una opcion (1-5): ").upper().strip()
            if bolsasOpc=="1":
                basicos.borrarPantalla()
                bolsas.agregarBolsas()
            elif bolsasOpc=="2":
                basicos.borrarPantalla()
                bolsas.borrarBolsa()
            elif bolsasOpc=="3":
                basicos.borrarPantalla()
                bolsas.mostrarBolsa()
            elif bolsasOpc=="4":
                basicos.borrarPantalla()
                bolsas.existenciasBolsas()
            elif bolsasOpc=="5":
                basicos.borrarPantalla()
                bolsas.vaciarBolsas()
            else:
                basicos.error()
        case "2":
            basicos.borrarPantalla()
            print("\n\t\t\t..::: \U0001F308 LAS MEZCLADITAS \U0001F308 :::... \n\t\t..::: \U0001F460 Sistema de Gestión de Zapatos \U0001F460 :::...\n\t\t\t 1️⃣- Agregar  \n\t\t\t 2️⃣- Borrar \n\t\t\t 3️⃣- Mostrar \n\t\t\t 4️⃣- Modificar \n\t\t\t 5️⃣- Vaciar")
            zapatosOpc=input("\n\t\t\t \U0001F4DD una opcion (1-5): ").upper().strip()
            if zapatosOpc=="1":
                basicos.borrarPantalla()
                zapatos.agregarZapatos()
            elif zapatosOpc=="2":
                basicos.borrarPantalla()
                zapatos.borrarZapatos()
            elif zapatosOpc=="3":
                basicos.borrarPantalla()
                zapatos.mostrarZapatos()
            elif zapatosOpc=="4":
                basicos.borrarPantalla()
                zapatos.existenciasZapatos()
            elif zapatosOpc=="5":
                basicos.borrarPantalla()
                zapatos.vaciarZapatos()
            else:
                basicos.error()
        case "3":
            basicos.borrarPantalla()
            print("\n\t\t\t..::: \U0001F308 LAS MEZCLADITAS \U0001F308 :::... \n\t\t..::: \U0001F490 Sistema de Gestión de Perfumes \U0001F490 :::...\n\t\t\t 1️⃣- Agregar  \n\t\t\t 2️⃣- Borrar \n\t\t\t 3️⃣- Mostrar \n\t\t\t 4️⃣- Modificar \n\t\t\t 5️⃣- Vaciar")
            zapatosOpc=input("\n\t\t\t \U0001F4DD una opcion (1-5): ").upper().strip()
            if zapatosOpc=="1":
                basicos.borrarPantalla()
                perfumes.agregarPerfumes()
            elif zapatosOpc=="2":
                basicos.borrarPantalla()
                perfumes.borrarPerfumes()
            elif zapatosOpc=="3":
                basicos.borrarPantalla()
                perfumes.mostrarPerfumes()
            elif zapatosOpc=="4":
                basicos.borrarPantalla()
                perfumes.existenciasPerfumes()
            elif zapatosOpc=="5":
                basicos.borrarPantalla()
                perfumes.vaciarPerfumes()
            else:
                basicos.error()
        case "4":
            basicos.borrarPantalla()
            print("\n\t\t\t..::: \U0001F308 LAS MEZCLADITAS \U0001F308 :::... \n\t\t..::: \U0001F511 Sistema de Gestión de Llaveros \U0001F511 :::...\n\t\t\t 1️⃣- Agregar  \n\t\t\t 2️⃣- Borrar \n\t\t\t 3️⃣- Mostrar \n\t\t\t 4️⃣- Modificar \n\t\t\t 5️⃣- Vaciar")
            zapatosOpc=input("\n\t\t\t \U0001F4DD una opcion (1-5): ").upper().strip()
            if zapatosOpc=="1":
                basicos.borrarPantalla()
                llaveros.agregarLlaveros()
            elif zapatosOpc=="2":
                basicos.borrarPantalla()
                llaveros.borrarLlaveros()
            elif zapatosOpc=="3":
                basicos.borrarPantalla()
                llaveros.mostrarLlaveros()
            elif zapatosOpc=="4":
                basicos.borrarPantalla()
                llaveros.existenciasLlaveros()
            elif zapatosOpc=="5":
                basicos.borrarPantalla()
                llaveros.vaciarLlaveros()
            else:
                basicos.error()
        case "5":
            basicos.borrarPantalla()
            opcion=False
            print("\n\t`\u2705`Terminaste la ejecucion del SW`\u2705`")
            basicos.esperarTecla()
        case _:
            basicos.borrarPantalla()
            input("\n\t`\u274C`Opción invalida vuelva a intentarlo ... por favor`\u274C`")
