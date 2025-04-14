# Repetir una palabra

palabra = input('Ingrese una palabra:\n')
numero = int(input('Ingrese cantidad a repetir:\n'))

for p in range(numero):
    print(palabra)
    
while numero > 0:
    print(palabra)
    numero -= 1
    

    
