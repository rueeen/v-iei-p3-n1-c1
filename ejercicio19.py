# Agregar datos a una lista

lista = [] # lista vacia
print(lista)

# Agregando elementos a lista con append
lista.append('Eustacio') # Metodo de lista, agrega algo al final de la lista
print(lista)

lista.append('Perico')
# lista.append('Maria', 'Jose') ERROOR
print(lista)

# Agregando elementos a lista con insert
lista.insert(1, 'Maria') # Agrega algo a la lista en el indice indicado
print(lista) # Eustacio, Maria, Perico
lista.insert(100000, 'Jose') 
print(lista)