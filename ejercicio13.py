# Funciones

# Validar que un numero ingresado sea positivo
'''
numero_1 = int(input('Ingrese numero:\n'))

while numero_1 < 0:
    print('Debe ingresar solo numeros positivos!')
    numero_1 = int(input('Ingrese nuevamente:\n'))

numero_2 = int(input('Ingrese numero:\n'))

while numero_2 < 0:
    print('Debe ingresar solo numeros positivos!')
    numero_2 = int(input('Ingrese nuevamente:\n'))
'''
#               NO Parametros
def validar_numero():
    num = int(input('Ingrese un numero positivo:\n'))
    while num <= 0:
        print('Debe ingresar solo numeros positivos!')
        num = int(input('Ingrese nuevamente:\n'))
    # Retorno
    return num
print('Primer numero')
num1 = validar_numero()
print('Segundo numero')
num2 = validar_numero()

print(num1, num2)