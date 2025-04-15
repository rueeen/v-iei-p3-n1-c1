# Eliminar elementos de una lista

lista = [1, 2, 3, 4, 5]

# Eliminar por indice
del lista[3] # Esto elimina el numero 4

print(lista)

lista.pop() # Cuando no se indica el indice elimina siempre el ULTIMO 5
print(lista) # 1, 2, 3

# Eliminar por valor
lista.remove(1) # Elimina el numero 1
print(lista) # 2, 3
# lista.remove(10) # Esto da error porque no existe el numero 10 en la lista

numeros = [1, 2, 3, 1, 2, 1]
resp = numeros.remove(1)
print(numeros) # 2, 3, 1, 2, 1 ELIMINA UNO A LA VEZ Y EL PRIMERO QUE ENCUENTRA
# print(resp) remove no retorna

eliminada = numeros.pop(3) # ELimina por indice, tambien retorna
print(f'Se elimino el numero {eliminada} de la lista')