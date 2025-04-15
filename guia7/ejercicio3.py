def validar_par(num):
    if num % 2 == 0:
        return True
    return False

num = int(input('Ingrese numero entero:\n'))

resultado = validar_par(num)

if resultado == True:
    print('Es PAR')
else:
    print('ES IMPAR')