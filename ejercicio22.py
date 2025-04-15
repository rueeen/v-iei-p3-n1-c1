# Recorrer listas

lista = ['Perico', 'Eustacio', 'Maria']

for elemento in lista:
    print(elemento)
    
indice = 0
while indice < len(lista):
    print(f'Indice: {indice} -> Valor {lista[indice]}')
    indice += 1
    
