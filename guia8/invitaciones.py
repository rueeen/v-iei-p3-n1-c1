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
        nombre = input('Ingrese nombre invitado:\n').capitalize()
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
        nombre = input('Ingrese nombre a cambiar:\n').capitalize() # maria LAS PETUNIAS -> Maria Las Petunias
        if nombre in invitados: # True si nombre existe
            nuevo_nombre = input('Ingrese nuevo nombre:\n').capitalize()
            # Modificando lista
            invitados[invitados.index(nombre)] = nuevo_nombre # Metodo index devuelve el indice de un elemeto EJ: lst = [ 'a', 'b', 'c' ]  -> lst.index('b') -> 1
            print('Se ha modificado el nombre de invitado')
        else:
            print('Invitado no existe')
                    
    elif opcion == '4':
        print('==== Eliminar invitados =====')
        nombre = input('Ingrese nombre a eliminar:\n').capitalize()
        if nombre in invitados:
            invitados.remove(nombre)
            print(f'Se elimino el invitado {nombre}')
        else:
            print('No se encontro al invitado')
        
    elif opcion == '0':
        print('==== Salir =====')
        print('Saliendo del sistema...')
        break

    else:
        print('Opcion ingresada no valida')