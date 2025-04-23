# Ejemplo try - except
# Que es una excepcion

# numero = 'Cinco'
# numero = int(numero) Esto da error porque 'cinco' no tiene una conversion a int

# Las excepciones son errores que no podemos controlar o esperar
valor = False
while valor == False:
    try:
        # Un bloque que puede producir un error
        numero1 = int(input('Ingrese un numero:\n'))
        valor = True
    except ValueError as e: # dando un alias al error
        # Un bloque que se ejecuta en caso de algun error provado en el cuerpo del try
        print('No se puede convertir numero a entero, intente otra vez')
        print(e)
    except:
        print('Error generico')
    
print(f'Tu numero es {numero1}') 