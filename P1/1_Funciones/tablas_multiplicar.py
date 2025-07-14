'''
Crear un programa que calcule e imprima cualquier tabla de multiplicar

Requisitos:
1.- Sin estructuras de control
2.- Sin funciones
'''
#version 1
'''
num=int(input("Dame el número de la tabla de multiplicar a calcular: "))
tabla=num*1
print(f"{num} x 1 = {tabla}")
tabla=num*2
print(f"{num} x 2 = {tabla}")
tabla=num*3
print(f"{num} x 3 = {tabla}")
tabla=num*4
print(f"{num} x 4 = {tabla}")
tabla=num*5
print(f"{num}2 x 5 = {tabla}")
tabla=num*6
print(f"{num} x 6 = {tabla}")
tabla=num*7
print(f"{num} x 7 = {tabla}")
tabla=num*8
print(f"{num} x 8 = {tabla}")
tabla=num*9
print(f"{num} x 9 = {tabla}")
tabla=num*10
print(f"{num} x 10 = {tabla}")

'''
#version 2
"""
for i in range(1,11):
    tabla=num*i
    i+=1
    print(f"{num} x {i} = {tabla}")

    num=int(input("Dame el número de la tabla de multiplicar a calcular: "))

    
i=1
while i<=10:
    tabla=num*i
    print(f"{num} x {i} = {tabla}")
    i+=1
"""

#Version 3

def mult(numero):
    num=numero
    respuesta=""
    for i in range(1,11,1):
        tabla=num*i
        respuesta+=f" \n {num} x {i} = {tabla} \n"
    return respuesta

numero=int(input("Dame el número de la tabla de multiplicar a calcular: "))
result=mult(numero)
print(f"{result}")
    