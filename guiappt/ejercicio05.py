nombre = input('Ingrese su nombre:\n')
apellido = input('Ingrese su apellid:\n')

# concatenando
correo = nombre + '.' + apellido + '@correo.cl'
print(f'El correo es: {correo}')
print(f'El correo es: {nombre + '.' + apellido + '@correo.cl'}')
# utilizando directamente print
print(f'El correo es: {nombre}.{apellido}@correo.cl')

print(nombre, '.', apellido, '@correo.cl') # NO SIRVE
print(nombre, '.', apellido, '@correo.cl', sep='') # SI SIRVE