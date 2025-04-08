pies = float(input('Ingrese pies a convertir:\n'))
constante = 0.3048

metros = pies * constante

print(f'Los {pies} pies a metros son: {metros}')# tiene muchos decimales a veces\
# aca utilizaremos round(valor a redondear, la cantidad de decimales)
print(f'Los {pies} pies a metros son: {round(metros, 2)}')