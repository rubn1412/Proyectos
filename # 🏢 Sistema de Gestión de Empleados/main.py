from Empresa import *
from Empleado import *
empleado = Empleado("","")
empresa = Empresa ("")

while True :
    print(""" Menu
    1. Contratar Empleados
    2. Total Empleados
    3. Empleados por departamento
    4. Salir
    """)
    opcion = int(input("Introduzca opcion: "))
    if opcion == 1:
        empleado.nombre = input("Introduzca Nombre Empleado: ")
        empleado.departamento= input("Introduzca Departamento: ")
        empresa.contratarEmpleados(empleado.nombre,empleado.departamento)
        print("Empleado Registrado")
    elif opcion == 2:
        print("Total de Empleados en la Empresa")
        print(empleado.contadorTotal())
    elif opcion == 3:
        print("Empleados por Departamento: ")
        empresa.numeroEmpleadosXDepartamento()
    elif opcion == 4:
        print("Hasta luego!")
        break
    else: print("Opcion no valida")
