from paquete1 import modulos

print(modulos.saludar("Adele"))

modulos.borrarPantalla()
nom,tel=modulos.solicitarDatos2()
print(f"\n\t.:: Agenda Telefonica ::.\n\t\tNombre:{nom}\n\t\tTelefono:{tel}")
modulos.espereTecla()

