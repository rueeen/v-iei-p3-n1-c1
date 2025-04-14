# validar que numero sea positivo
numero = -1
while numero <= 0:
    numero = int(input('Ingrese un numero positivo:\n'))

final = ', '
for i in range(1, numero + 1):
    if i % 2 != 0:
        print(i, end=final)
        
        