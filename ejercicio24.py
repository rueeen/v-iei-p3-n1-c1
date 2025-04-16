# 2 listas DISTINTAS
# Clon
#          0  1  2  3
lista_a = [1, 2, 3, 4]
#            [inicio:fin] el fin menos 1
lista_b = lista_a[0:3]
lista_b[2] = 100 # [1, 2, 100]

print(lista_b)
print(lista_a)

lista_c = lista_a[:] # Copia la lista completa
lista_d = lista_a[:2] # Copia desde el inicio hasta el indice 1 de la lista
lista_e = lista_a[1:] # Copia desde el indice 1 hasta el final
#         -4   -3   -2   -1
listas = ['a', 'b', 'c', 'd']
listas[-1] = 'z' # ['a', 'b', 'c', 'z']

# Copia completa
lista_a_clon = lista_a.copy() # Metodo para copiar la lista completa