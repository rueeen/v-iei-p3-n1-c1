# validar que numero sea positivo
numero = -1
while numero <= 0:
    numero = int(input('Ingrese un numero positivo:\n'))

final = ', '
for i in range(numero, -1, -1):
    if i == 0:
        final = '\n'
    print(i, end=final)