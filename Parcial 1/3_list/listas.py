import os
#Ejemplo 1: Crear una lista de numeros e imprimir el contenido

numeros=[1,2,3,4,5]
print(numeros)

for i in numeros:
    print(i)

for i in range(0,len(numeros)):
    print(numeros[i])


#Ejemplo 2: Crear una lista de palabras y posteriormente buscar la coinciencia de una palabra
os.system("cls")
palabras=["Hola", "Adios", "Numeros","Palabras"]
print(palabras)
palabra_buscar=input("Dame la palabra a buscar: ")

#1era forma
if palabra_buscar in palabras:
    print("Si se encontró la palabra")
    print(f"el numero de veces que se encontro la palabra es: {palabras.count(palabra_buscar)}")
else:
    print("No se encontró la palabra")

#2da forma
encontro=False
for i in palabras:
    if i==palabra_buscar:
        encontro=True
    
if encontro:
    print("Si encontro la palabra")
else:
    print("no se encontro la palabra")

#3ra forma
encontro=False
for i in range(0,len(palabras)):
    if palabras[i]==palabra_buscar:
        encontro=True
    
if encontro:
    print("Si encontro la palabra")
else:
    print("no se encontro la palabra")

input("Oprima tecla para continuar")


#ejemplo 3 Añadir elementos a una lista
os.system("cls")
numeros=[]
print(numeros)
opc=True
while opc:
    numero=float(input("Dame un numero entero o decimal: "))
    numeros.append(numero)
    resp=input("¿deseas agregar otro numero?: ").lower()
    if resp=="si":
        opc=True
    else:
        opc=False

print(numeros)
input("Oprima tecla para continuar")

#Ejemplo 4: Crear una lista multidimensional que sea una agenda

agenda=[
       ["Carlos","6181234567"],
       ["Alberto","667123456"],
       ["Martin","678123456"]
       ]
print(agenda)

for i in agenda:
    print(i)

for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])

cadena=""
for r in range(0,3):
    for c in range(0,2):
        cadena+=f"{agenda[r][c]},"
        cadena+="\n"
print(cadena)
    