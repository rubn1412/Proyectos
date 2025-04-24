inventario = [
    {'id':1, "Nombre":"Camisa", 'Precio': 25.99, 'Cantidad':50 },
    {'id':2, "Nombre": "Pantalon", 'Precio': 39.99 , 'Cantidad': 30},
    {'id':3, "Nombre": "Zapatos", 'Precio': 49.99, 'Cantidad': 20}
]
def mostrarInventario():
    print(f'------Inventario Almacen ------')
    for i in inventario:
        print(f'Id :{i.get("id")}, Nombre: {i.get("Nombre")} '
              f'Precio: {i.get("Precio")} Cantidad: {i.get("Cantidad")}' )
def agregarProducto():
    print("Agregar Producto")
    id = int(input('Introduzca ID:'))
    nombre = input('Introduzca Nombre:')
    precio = float(input('Introduzca Precio:'))
    cantidad = int(input('Introduzca Cantidad:'))
    nuevoProducto={'id':id, 'Nombre':nombre, 'Precio': precio, 'Cantidad':cantidad}
    inventario.append(nuevoProducto)

def buscarId():
    print("Buscar Prodcuto:")
    id_buscar=int(input("Introduzca el Id a buscar: "))
    for i in inventario:
        if i.get("id") == id_buscar:
            print("Producto Encontrado")
            print(f'Id :{i.get("id")}, Nombre: {i.get("Nombre")} '
                  f'Precio: {i.get("Precio")} Cantidad: {i.get("Cantidad")}')
            return
while True:
    print(""" Menu
    1 - Mostrar Inventario
    2 - Agregar Producto
    3 - Buscar Producto
    4 - Salir
    """)
    opcion = int(input("Introduzca Opcion (1-4):"))
    if opcion == 1:
        mostrarInventario()
    elif opcion == 2:
        agregarProducto()
    elif opcion == 3:
        buscarId()
    elif opcion == 4:
        print("Hasta luego!")
        break
    else: print("Opcion no valida")
