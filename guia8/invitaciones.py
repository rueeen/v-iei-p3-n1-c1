# Ejercicio para ingresar personas a una lista de invitados
# Podemos agregar personas a la lista           C reate
# Mostrar los invitados                         R read
# Modificar nombres de persona de la lista      U pdate
# Eliminar personas a la lista                  D elete

invitados = [] 
while True:
    print('==== Menu de acciones ====')
    print('1. Agregar invitado a lista')
    print('2. Mostrar invitados')
    print('3. Modificar nombre invitado')
    print('4. Eliminar invitado')
    print('0. Salir')

    opcion = input('Ingrese su opcion:\n')
    
    if opcion == '1':
        print('==== Agregar invitado =====')
        nombre = input('Ingrese nombre invitado:\n')
        invitados.append(nombre)
        print(f'Se agrego a {nombre} a la lista!')
        
    elif opcion == '2':
        print('==== Mostrar invitados =====')
        contador = 1
        for i in invitados:
            print(f'{contador}. Nombre: {i}')
            contador += 1
        
    elif opcion == '3':
        print('==== Modificar invitados =====')
        
    elif opcion == '4':
        print('==== Eliminar invitados =====')
        
    elif opcion == '0':
        print('==== Salir =====')
        
    else:
        print('Opcion ingresada no valida')