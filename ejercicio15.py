# Ejercicios palabra clave y keyword

def saludar(nombre, apellido):
    print(f'Mi nombre es {apellido}, {nombre} {apellido}')
    
n = 'James'
a = 'Bond'

saludar(n, a) # Mi nombre es Bond, James Bond
saludar(nombre = a, apellido = n) # Mi nombre es James, Bond James
saludar(nombre = a, apellido= a) # Mi nombre es Bond, Bond Bond
# saludar(a) # Error

# Parametros con valores por defecto
def suma(a = 5, b = 3):
    print(a + b)
    
suma(3, 8) # 11
suma(3) # 6
suma(b = 2) # 7
suma() # 8

# CUIDADO CON ESTO
# suma(b = 2, b = 3) # Error