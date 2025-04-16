lista_a = [1, 2, 3, 4, 5]
lista_b = lista_a

lista_b.append(6) # [1, 2, 3, 4, 5, 6]
lista_a[2] = 100 # [1, 2, 100, 4, 5]

print(lista_b) # [1, 2, 100, 4, 5, 6]
print(lista_a) # [1, 2, 100, 4, 5, 6]


a = 5
b = a 

print(a) # 5
print(b) # 5

b += 1
print(a) # 5
print(b) # 6