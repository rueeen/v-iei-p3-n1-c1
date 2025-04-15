def contar_vocales(palabra):
    contar = 0
    for c in palabra:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            contar += 1
            
    print(f'La cantidad de vocales (a,e,i,o,u) son: {contar}')
            
palabra = input('Ingrese palabra:\n').lower() # Nos aseguramos siempre minusculas

contar_vocales(palabra)


