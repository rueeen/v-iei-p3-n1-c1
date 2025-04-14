# Contar caracteres "a"

# Dato entrada -> paralelepipedo 
# Dato salida  -> 2 letras "a"

palabra = input('Ingrese una palabra:\n')
# Variable para contar las letras
contador_a = 0

for i in palabra:
    # i representa cada caracter de la palabra
    if i == 'a' or i == 'A':
        contador_a += 1 # Incrementa el contador en 1

# Dato salida
print(f'La cantidad de letras "a" que hay en la palabra son: {contador_a}')