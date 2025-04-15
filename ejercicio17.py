# SCOPE
numero = 10

def mostrar_numero():
    numero = 20
    print(numero)
    
mostrar_numero() # 20
print(numero) # 10

def crear_variable():
    nombre = 'Perico los palotes'
    
#print(nombre) Esto da error 

def variable_global():
    global edad
    edad = 10
    
print(edad)