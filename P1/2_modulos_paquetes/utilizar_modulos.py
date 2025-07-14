#Priemer utilzar modulos
import modulos

modulos.borrarPantalla
print(modulos.saludar("sadffgj"))

# segunda forma utilizar modulos

from modulos import saludar,borrarPantalla
#borrarPantalla()
print(saludar("asdgjklg"))

nombre=input("Ingresa el nombre del contacto: ")
telefono=input("Ingresa el número de telefono: ")

nom,tel=modulos.solicitarDatos4(nombre,telefono)

print(f"\tnombre completo: {nom}\n\ttelefono: {tel}")