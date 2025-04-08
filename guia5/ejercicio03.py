palabra1 = input('Ingrese palabra:\n').capitalize()
palabra2 = input('Ingrese otra palabra:\n').capitalize()

# formateadores de texto
palabra3 = 'PeRro'
palabraMayuscula = palabra3.upper() # todo mayuscula
print(palabraMayuscula)
palabraMinuscula = palabra3.lower() # todo minuscula
print(palabraMinuscula)
palabraMayusMinus = palabra3.capitalize() # primera letra mayus resto minus
print(palabraMayusMinus)

if palabra1 == palabra2:
    print('Son iguales')
else:
    print('No son iguales')