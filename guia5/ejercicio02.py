numero1 = int(input('Ingrese un numero:\n'))
numero2 = int(input('Ingrese otro numero:\n'))

if numero1 > numero2:
    print(f'El numero {numero1} es mayor')
elif numero1 < numero2:
    print(f'El numero {numero2} es mayor')
else:
    print('Son iguales')