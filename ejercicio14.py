# Funciones
# Sin parametros
def sumar_numeros():
    a = 5
    b = 3
    print(a + b) # 8
    
# invocar funcion
sumar_numeros()

def sumar_numeros_parametros(a, b):
    print(a + b)
    
# Invocar funcion con parametros
sumar_numeros_parametros(5, 7) # 12
sumar_numeros_parametros(12, 7) # 19
# sumar_numeros_parametros(5) # Error
sumar_numeros_parametros(-12, 7) # -5

def dividir_numeros_parametros(a, b):
    print(a / b)
    
dividir_numeros_parametros(2, 4) # 0.5
dividir_numeros_parametros(4, 2) # 2.0
a = 4
b = 8
# ARGUMENTOS POSICIONALES
dividir_numeros_parametros(b, a) # 2.0

# ARGUMENTOS POR PALABAR CLAVE
dividir_numeros_parametros(b = b, a = a)