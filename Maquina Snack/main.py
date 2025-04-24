inventario = [
    {"id": 1, "nombre": "Papas", "Precio":30 },
    {"id": 2, "nombre": "Refresco", "Precio":50 },
    {"id": 3, "nombre": "Sandwich", "Precio":120 }
]

listaCompra = []

def mostrar_inventario():
    print("Lista de Productos:")
    for i in inventario:
        print(f'Id:{i.get("id")} --> {i.get("nombre")} -- {i.get("Precio")} ')

def comprar():
    print("Menu de compra")
    idc=int(input("Introduzca Id a comprar:"))
    for i in inventario:
        if idc == i.get("id"):
            id = i.get("id")
            nombre = i.get("nombre")
            precio = i.get ("Precio")
            compras={"id": id, "nombre": nombre, "Precio":precio }
            listaCompra.append(compras)
            print(f' Id: {i.get("id")} -- {i.get("nombre")} -- {i.get("Precio")}')
            print (f'Compra Registrada')
    else: print("Id no encontrado")

def mostrar_ticket():
    total = 0
    print("Ticket de Compra")
    for i in listaCompra:
        print(f' Id: {i.get("id")} -- {i.get("nombre")} -- {i.get("Precio")}')
        total += i.get("Precio")
    print (f'Total a Pagar: {total}')

while True:
    print("""Menu
    1. Mostrar Productos
    2. Comprar Productos
    3. Mostrar tickets
    4. Salir
    """)
    opcion= int(input("Seleccion Opcion (1-4): "))
    if opcion == 1:
        mostrar_inventario()
    elif opcion == 2:
        comprar()
    elif opcion == 3:
        mostrar_ticket()
    elif opcion == 4:
        print("Hasta Luego")
        break
    else:
        print("Introduzca una opcion validad")


