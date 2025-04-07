# ejemplos condicion if

# Verificar si alguien es mayor o menor de edad
edad = int(input('Ingrese su edad:\n'))

# Estructura de decision
if edad >= 18:
# Cuerpo si la condicion es True
    print('Usted es mayor de edad')
else:
    print('Usted es menor de edad')
    
print('Esto esta fuera del if')

# if anidado
# Ordenar 3 numeros de mayor a menor
a = 5
b = 3
c = 10

if a > b and a > c :
    print(f'El mayor es {a}')
    if b > c :
        print(f'El medio es {b}')
        print(f'El menor es {c}')
    else:
        print(f'El medio es {c}')
        print(f'El menor es {b}')
# Volve a preguntar
elif b > a and b > c :
    print(f'El mayor es {b}')
    if a > c:
        print(f'El medio es {a}')
        print(f'El menor es {c}')
    else:
        print(f'El medio es {c}')
        print(f'El menor es {a}')
else:
    print(f'El mayor es {c}')
    if a > b:
        print(f'El medio es {a}')
        print(f'El menor es {b}')
    else:
        print(f'El medio es {b}')
        print(f'El menor es {a}')