# Metodos adicionales

lista = ['a', 'b', 'c', 'b']

print(lista.index('b')) # Muetra el indice de un valor -> 1
# print(lista.index('e')) # Error

lista_reversa = lista.reverse() # Crea una lista al revez la lista
print(lista_reversa) # ['b', 'c', 'b', 'a']

lista_ordenada = lista.sort() # Crea una lista ordenada de la original
print(lista_ordenada) # ['a', 'b', 'b', 'c'] 

lista = [1, 2 , 'a', 'B']
#lista.sort() # Error