# utilizando input para recibir datos desde consola

# Vamos a sumar 2 numeros
num1 = input('Ingrese un numero:\n') # 2 de tipo str
num2 = input('Ingrese otro numero: ') # 3 de tipo str

# Recordar que input siempre devuelve el valor como STRING
resultado = num1 + num2 # 23
print(f'Aca hay concatenacion y el resultado es: {resultado}')

num3 = int(input('Ingrese un numero:\n')) # 2 de tipo int
num4 = float(input('Ingrese otro numero:\n')) # 3 de tipo float

# Ahora si sumamos si se aplicara la operacion matematica
resultado = num3 + num4
print(f'Aca hay suma y el resultado es: {resultado}')