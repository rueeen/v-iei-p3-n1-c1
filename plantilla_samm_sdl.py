
# =========================
# Sistema de Gestión de Productos con Seguridad (SAMM / SDL)
# =========================

# Listas de datos
usuarios = [
    {'usuario': 'admin', 'password': '1234', 'nombre': 'Perico', 'apellido': 'Los palotes', 'rut':'111-1'}
    ]  # Lista para almacenar los usuarios
productos = []  # Lista para almacenar los productos

# Función para registrar un usuario
def registrar_usuario():
    print("=== Registro de Usuario ===")

# Función para iniciar sesión
def iniciar_sesion():
    print("=== Inicio de Sesión ===")
    usuario = input('Ingrese su su usuario: ').lower()
    password = input('Ingrese su password: ')
    
    for u in usuarios:
        if u['usuario'] == usuario and u['password'] == password:
            print('Usuario encontrado!')
            return u
    return None

# Menú principal de usuarios
def menu_usuarios():
    while True:
        print("===== MENÚ DE USUARIOS =====")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            pass
        elif opcion == "2":
            iniciado = iniciar_sesion()
            if iniciado is not None:
                
                menu_productos(iniciado)
            else:
                print('Datos incorrectos')
        
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")

# Funciones de productos
def agregar_producto(rut_usuario):
    print("=== Agregar Producto ===")

def mostrar_productos(rut_usuario):
    print("=== Productos del Usuario ===")

def modificar_producto(rut_usuario):
    mostrar_productos(rut_usuario)

def eliminar_producto(rut_usuario):
    mostrar_productos(rut_usuario)

# Menú de productos
def menu_productos(iniciado):
    print(f'Bienvenido: {iniciado["nombre"]} {iniciado["apellido"]}')  
    while True:
        print("===== MENÚ DE PRODUCTOS =====")
        print("1. Agregar producto")
        print("2. Mostrar mis productos")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("5. Cerrar sesión")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            modificar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

# Ejecutar menú de usuarios al iniciar
menu_usuarios()

