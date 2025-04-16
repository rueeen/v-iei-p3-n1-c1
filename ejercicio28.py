diccionario = {'nombre': 'Perico', 'apellido': 'Los Palotes'}

# Eliminar
del diccionario['nombre'] # Elimina la clave y valor de nombre
print(diccionario) # {'apellido':'Los Palotes'}

diccionario.pop('apellido') # Elimina el ultimo key:value del diccionario
print(diccionario) # {}

numeros = {1:1, 2:2, 3:3, 4:4}
numeros.clear() # Vacia diccionario
print(numeros) # {}