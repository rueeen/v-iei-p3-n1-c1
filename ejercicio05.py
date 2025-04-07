# DATO DE ENTRADA
# funcion input()

input('Escriba algo: ')

# Si quiero que escriba debajo
input('Escriba debajo:\n') # \n representa un salto de linea

# input es una funcion que RETORNA
# input debe ir acompañado de una variable
nombre = input('Ingrese su nombre:\n')
print(f'Hola {nombre} eres bienvenido')

# Detalles: input() siempre devuelve el valor en tipo str
a = input('Ingrese un numero:\n') # 3
b = input('Ingrese otro numero:\n') # 5
c = a + b # str + str -> strstr
print(c) # 35

