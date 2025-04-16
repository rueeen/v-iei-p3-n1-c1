# Modificar diccionario

datos = {
    'nombre': 'Perico',
    'apellido': 'Las petunias',
    'edad': 40
}

# Moficando apellido
datos['apellido'] = 'Los palotes'
# Esto no da error, lo que haces agregar la key:valor direccion
datos['direccion'] = 'Av falsa 123' # AGREGAR NUEVOS DATOS A DICT
print(datos)

# Actualizar utilizando metodo update
datos.update({'apellido':'Valencia', 'ciudad':'Arica'})
print(datos)