# import
import os # Importar una libreria para manipular el SO (sistema operativo)

# funciones
def buscar_contacto(nombre, apellido):
    # [ {}, {}, {} ]
    for contacto in agenda: # contacto = {'nombre':'Perico', 'apellido':'',....}
        if contacto['nombre'] == nombre and contacto['apellido'] == apellido:
            # contacto encontrado
            return contacto # {'nombre':'Perico', 'apellido':'Los palotes',....}
    return None

#codigo
# Nuestros contactos tendran nombre, apellido, numero y si son favoritos
# Creamos lista antes de ciclo para que no se resetee
agenda = [] # Una lista vacia
# Menu de acciones
while True:
    # Limpiar pantalla
    os.system('cls')
    print('==== Menu de opciones ====')
    print('1. Agregar contacto    C')
    print('2. Mostrar contactos   R')
    print('3. Modificar contacto  U')
    print('4. Eliminar contacto   D')
    # 5. Cambiar contacto a favorito Boolean
    # 6. Eliminar contactos no favoritos
    print('0. Salir')
    
    opcion = input('Ingrese opcion:\n')
    # Limpiar pantalla
    os.system('cls')
    
    if opcion == '1':
        print('==== Agregar contacto ====')
        # Datos de entrada
        nombre = input('Ingrese nombre contacto:\n').capitalize()
        apellido = input('Ingrese apellido contacto:\n').capitalize()
        
        # Agregar verificacion para que nombre y apellido no sean vacios ''
        
        # Verificacion
        resultado = buscar_contacto(nombre, apellido) # Retorna un contacto {} o None
        
        if resultado is not None:
            # Contacto existe
            print('Contacto ya esta registrado')
            input('Presione enter para continuar...') # Para que alcanzar a leer el mensaje
            continue
        
        numero = int(input('Ingrese numero contacto:\n'))
        
        # Verificar que numero no sea vacio y que tenga 8 numeros
        
        # Este lo revisaremos de la siguiente forma
        favorito = input('Ingrese si es favorito:\n').lower()
        if favorito == 'si':
            favorito = True
        else:
            favorito = False
        persona = {
            'nombre': nombre,
            'apellido':apellido,
            'numero':numero,
            'favorito':favorito
            }        
        agenda.append(persona)
        print('Contacto agregado exitosamente!')
        
    elif opcion == '2':
        print('==== Mostrar contactos ====')
        if len(agenda) == 0:
            print('No hay contactos')
        else: 
            # agenda = [ {'nombre': '', 'apellido': '', 'numero': 0, 'favorito':True}, {...}, {...}]
            for c in agenda: # c = {'nombre': '', 'apellido': '', 'numero': 0, 'favorito':True}
                print(f'Nombre: {c["nombre"]} {c["apellido"]}')
                print(f'Numero: {c["numero"]}')
                print(f'Favorito: {c["favorito"]}') # Mostrar si o no en vez de True o False
                print('----------------------------------------------')
    elif opcion == '3':
        print('==== Modificar contacto ====')
        # Agregar editar
        # nombre
        # apellido
        # TAREA MODIFICAR NOMBRE Y APELLIDO
        nombre = input('Ingrese nombre a buscar:\n').capitalize()
        apellido = input('Ingrese apellido a buscar:\n').capitalize()
        resultado = buscar_contacto(nombre, apellido) # resultado = {'nombre':'', 'apellido':'', 'numero':0, 'favorito':True} o None
        if resultado is not None:
            # Lo encontre
            nuevo_numero = int(input('Ingrese nuevo numero del contacto:\n'))
            
            # Verificar que numero no sea vacio y que tenga 8 numeros
            
            resultado['numero'] = nuevo_numero
            print(f'Se ha cambiado numero del contacto {nombre} {apellido}')
        else:
            print('Contacto no encontrado')

    elif opcion == '4':
        print('==== Eliminar contacto ====')
        nombre = input('Ingrese nombre a eliminar:\n')
        apellido = input('Ingrese apellido a eliminar:\n')
        resultado = buscar_contacto(nombre, apellido)
        if resultado is not None:
            # Lo encontre
            agenda.remove(resultado)
            print('Contacto eliminado!')
        else:
            print('No se encontro contacto')
    elif opcion == '0':
        print('Saliendo programa...')
        break
    else:
        print('Opcion ingresda no valida...')

    input('Presione enter para continuar...')
    
# TAREA HASTA DOMINGO POR 1 punto