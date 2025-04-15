# Declarar funcion
def comparar_numeros(num1, num2):
    if num1 > num2:
        print(f"El mayor es: {num1}")
    elif num1 < num2:
        print(f"El mayor es: {num2}")
    else:
        print('Son iguales')
        
# Los datos a recibir para enviar a funcion
n = int(input('Ingrese un numero:\n'))
m = int(input('Ingrese segundo numero:\n'))        

# Invocacion funcion
comparar_numeros(n, m)