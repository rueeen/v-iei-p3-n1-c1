# Diccionarios

# Se componen de clave y valor

datos_personales = {
    #  k        v
    'nombre':'Perico',
    'apellido': 'Los Palotes',
    'edad': 40,
    'nombre': 'Maria'
}

print(datos_personales)

print(f"La edad de la persona es: {datos_personales['edad']}")
# print(f'La edad de la persona es: {datos_personales["Edad"]}') # Da error, key no existe

print(datos_personales.keys()) # Imprime solo las keys
print(datos_personales.values()) # Imprime solo los valores

print('Esta palabra resalta "comillas" ')
print("Esta palabra resalta 'comillas' ")
print("Esta palabra resalta comillas 'simples' y \"dobles\" ")