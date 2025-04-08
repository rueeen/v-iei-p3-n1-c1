precio = int(input('Ingrese precio producto:\n'))
descuento = int(input('Ingrese cantidad descuento:\n'))

precio_descuento = precio * descuento / 100

precio_final = precio - precio_descuento

print(f'Precio producto: {precio}')
print(f'Descuento producto: {precio_descuento}')
print('----------------------------------')
print(f'Valor final: {precio_final}')