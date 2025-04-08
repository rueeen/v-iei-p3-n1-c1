peso = float(input('Ingrese peso:\n'))
altura = float(input('Ingrese altura:\n'))

imc = peso / altura ** 2 # 15

if imc <= 15:
    print('Delgadez muy severa')
elif imc > 15 and imc < 15.9:
    print('Delgadez severa')
elif 15.9 >= imc <= 18.4:
    print('Delgadez')
# faltan elif
else:  
    print('Obesidad muy severa')