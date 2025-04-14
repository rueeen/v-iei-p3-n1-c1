# ciclo while

# funciona con una condicion
respuesta = 'si'

while respuesta == 'si':
    print('repitiendo ciclo...')
    respuesta = input('Desea continuar?\n').lower()
print('Estoo esta fuera del ciclo')

contador = 1
while contador <= 10:
    print(contador)
    contador += 1
else:
    print('Fin del ciclo')
    
while True:
    print('Esto es infinito')
    # instruccion break, sirve para romper ciclos
    opcion = input('Ingrese 0 para terminar:\n')
    if opcion == '0':
        print('Adios!')
        break
        print('Esto nunca se ejecuta')
        
print('Esto es esta fuera del ciclo')

# intruccion continue
for i in range(10): # 0 - 9
    if i == 8:
        continue
    print(i) # 0, 1, 2, 3, 4, 5, 6, 7, 
    
# instruccion pass
if True:
    pass

