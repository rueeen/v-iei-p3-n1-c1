# intruccion for

# podemos recorrer str o range() de numero
for caracter in 'palabra': # se recorren todos los caracteres
    print(caracter)

# primera forma de range
for i in range(10): # genera lista desde 0 hasta 9
    print(i)

# segunda forma de range
#           inicio, fin  
for n in range(2, 10):
    print(n)
# No da nada 
for n in range(20, 10): # inicio mayor que fin
    print(n)
    
# tercera forma de range
for m in range(1, 9, 2):
    print(m)

# No hace nada
for m in range(20, 9, 2):
    print(m)

# este si funciona con incremento negativo
for m in range(20, 9, -2):
    print(m)




