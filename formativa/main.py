import os

def buscar_productos(nombre):
    for producto in tienda:
        if nombre == producto['nombre']: # nombre es str y producto es dict, {'nombre':'te', 'precio':1}
            return producto
    return None

tienda = [] # Lista vacia llamada tienda
ventas = [] # Lista vacia llamada ventas

while True:
    os.system('cls')
    print('==== Menu de opciones ====')
    print('1. Agregar producto a tienda')
    print('2. Modificar producto de tienda')
    print('3. Eliminar producto de tienda')
    print('4. Listar productos de tienda')
    print('5. Vender productos')
    print('6. Mostrar total venta')
    print('0. Salir')
    
    opcion = input('Ingrese su opcion:\n')
    os.system('cls')
    if opcion == '1':
        print('==== Agregar productos ====')
        # Primero recibimos datos de producto
        nombre = input('Ingrese nombre de producto:\n').capitalize()
        precio = int(input('Ingrese precio producto:\n'))
        # Verificar si nombre existe en tienda
        resultado = buscar_productos(nombre)
        if resultado is not None:
            print('Producto ya existe.')
            input('Presione enter para continuar...')
            continue
        # Si producto no existe vamos a crearlo
        producto = {'nombre': nombre, 'precio': precio}
        tienda.append(producto)
        print('Se ha logrado agregar el producto')
        
    elif opcion == '2':
        print('==== Modificar producto ====')
        nombre = input('Ingrese nombre producto a modificar:\n').capitalize()
        nuevo_precio = int(input('Ingrese nuevo precio de producto:\n'))
        resultado = buscar_productos(nombre) # None o un dict {'nombre':'te', 'precio':1}
        if resultado is not None:
            resultado['precio'] = nuevo_precio
            print(f'Se ha modificado el precio del producto {resultado["nombre"]}')
        else:
            print('No se encontro producto')
    elif opcion == '3':
        print('==== Eliminar productos ====')
        nombre = input('Ingrese nombre a eliminar:\n').capitalize()
        resultado = buscar_productos(nombre)
        if resultado is not None:
            tienda.remove(resultado)
            print('Se elimino producto')
        else:
            print('No se encontro producto')
    elif opcion == '4':
        print('==== Mostrar productos ====')
        if len(tienda) == 0:
            print('No hay productos')
        else:
            for producto in tienda:
                print(f'Nombre: {producto["nombre"]} - ${producto["precio"]}')
                print('---------------------------------------')
    elif opcion == '5':
        print('==== Vender productos ====')
        nombre = input('Ingrese producto a vender:\n').capitalize()
        resultado = buscar_productos(nombre)
        if resultado is not None:
            # Lo encontramos y vamos a venderlo
            ventas.append({'nombre':resultado["nombre"], 'precio':resultado["precio"]}) 
            print(f'Se ha registrado venta de prodcuto {resultado["nombre"]}')
        else:
            print('Producto no encontrado')
    
    elif opcion == '6':
        total_ventas = 0
        
        if len(ventas) == 0:
            print('No hay productos')
            input('Presione enter para continuar...')
            continue
        
        print('LISTA VENTAS 1')
        for producto in ventas:
            print(f'Nombre: {producto["nombre"]} - ${producto["precio"]}')
            total_ventas += producto['precio']
        print('---------------------------------------')
        print(f'Total: {total_ventas}')
    
    elif opcion == '0':
        print('Saliendo sistema...')
        input('Presione enter para continuar...')
        break
    
    else:
        print('Opcion ingresada no valida')
        
    input('Presione enter para continuar...')