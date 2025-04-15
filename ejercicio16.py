# Funciones CON RETORNO
# NO RETORNA
def suma(a, b):
    print(a + b)
    
resultado = suma(3, 8) # 11
print(resultado) # None : La ausencia de valor

# Funcion con retorno
def suma(a, b):
    return a + b # Esto devuelve el valor de la suma al contexto de la invocacion
    print('Hola mundo') # Esto no se ejecuta

resultado = suma(3, 8) # 11
print(resultado)