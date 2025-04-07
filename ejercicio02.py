# podemos imprimir con la funcion print()

print('Hola mundo')

nombre = "perico"
apellido = "los palotes"

print(nombre, apellido) # utilizando propiedad sep
print(nombre + " " + apellido) # concatenacion
print('{} {}'.format(nombre, apellido)) # format
print(f'{nombre} {apellido}') # format moderno

# que pasa con sep = " "
print(nombre, apellido) # perico los palotes
print(nombre, apellido, sep="#") # perico#los palotes

# tambien tenemos end = '\n' (salto de linea)
print("Aca hay un salto de linea", end='\n')
print("Aca no hay salto de linea", end='FIN')
print('Esto aparece en la misma linea')
 