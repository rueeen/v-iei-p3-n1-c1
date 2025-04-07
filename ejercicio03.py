# Operaciones
# suma +
a = 5
b = 6
c = a + b
print(c) # imprimir solo el resultado
print('El resultado de la suma es:', c) # Imprime el resultado mas texto
# print('El resultado de la suma:'+c) # Esto da error
# La operacion suma solo puede ser entre datos numericos int + int o int + float
# Puedo sumar str con str y esto se llama CONCATENACION
palabra_1 = 'hola'
palabra_2 = "mundo"
palabra_3 = palabra_1 + palabra_2
print(palabra_3) # holamundo
palabra_4 = palabra_1 + ' ' +palabra_2
print(palabra_4) # hola mundo
# palabra_5 = "hola' # Esto da error

# Resta -
# Esta solo existe entre numeros int y float
a = 5
b = 6
c = a - b
d = b - a
print(c) # -1
print(d) # 1
print("El valor de la resta es:", d) # Funciona
print("El valor de la resta es: {}".format(d)) # Funciona
print(f"El valor de la resta es: {d}") # Funciona
# print("El valor de la resta es: " + d) # NO FUNCIONA

# Ejemplo
nombre = "Perico"
apellido = "Los palotes"
edad = 99
direccion = "Av falsa 123"

# Sr nombre apellido, usted vive en direccion y tiene edad años
print("Sr", nombre, apellido, ", usted vive en direccion", direccion, "y tiene", edad, "años.")

print(f"Sr {nombre} {apellido}, usted vive en direccion {direccion} y tiene {edad} años.")
print("Sr {} {}, usted vive en direccion {} y tiene {} años.".format(nombre, apellido, direccion, edad))

# Multiplicacion *
a = 5
b = 6
c = 4.1
d = .5 # Esto equivale a 0.5

resultado = a * c
print(resultado)
# Una multiplicacion da como resultado un int si son ambos operadores int
# Si alguno de ellos o ambos son float, el resultado es float
a = 5
b = 3.0
c = a * b # 15.0 FLOAT
d = 3
e = a * d # 15 INT

# con * puedo hacer str * int
palabra = 'Repetir'
numero = 5 
print(palabra * numero) # RepetirRepetirRepetirRepetirRepetir
print((palabra + " ") * numero) # Repetir Repetir Repetir Repetir Repetir

# Division /
a = 5
b = 2
c = a / b # 2.5
# La division SIEMPRE da un resultado float
a = 6
b = 3
c = a / b # 2.0
# Ejemplo mal
d = 4,5 # NO ES FLOAT ES UNA TUPLA ()
e = 3
r = d * e
print(r)

numero = 1_0_0_0 # 1000
numero = 1_1_2_0_0_0 # 112000
print(numero)

numero = .0_01 # 0.001
print(numero)

numero = 2e2 # 2.0 e hace que se mueva la coma hacia la derecha 2 veces -> 200.0
print(numero)

numero = 2e-1 # 2.0 e hace que se mueva la coma hacia la izquierda 1 vez -> 0.2
print(numero)

# ESPECIALES

# Exponente
a = 5
b = 2
c = a ** b # 25, a es base y b exponente

# MOD 
a = 5
b = 3
c = a % b # 2 