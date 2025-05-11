import psycopg2
conexion = psycopg2.connect(user ='postgres', password ='admin', host = '127.0.0.1,', port = '5432', database = 'Persona')
while (True):
    print(""" 1. Agregar Persona
              2. Mostrar Registros
              3. Buscar Por ID
              4. Eliminar registro
              5. Eliminar Base de datos
              6. Salir
    
    """)
    opcion = int(input("Introduzca Opcion: "))
    if opcion == 1:
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s,%s,%s)'
                    nombre = input("Introduzca Nombre: ")
                    apellido = input("Introduzca Apellido: ")
                    email = input("Introduzca Email: ")
                    llave = (nombre,apellido,email)
                    cursor.execute(sentencia,llave)
                    conexion.commit()
                    print("Registado!")
        except Exception as e:
         print(f'Ocurrio un error  {e}')

    if opcion == 2:
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = 'SELECT * FROM persona'
                    cursor.execute(sentencia)
                    registro = cursor.fetchall()
                    print(registro)
        except Exception as e:
            print(f'Ocurrio un error  {e}')
    if opcion == 3:
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = "SELECT * FROM persona WHERE id_persona = %s"
                    id= input("Introduzca ID: ")
                    valor = (tuple(id),)
                    cursor.execute(sentencia,valor)
                    registro = cursor.fetchone()
                    print(registro)
        except Exception as e:
            print(f'Ocurrio un error {e}')
    if opcion == 4:
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = "DELETE FROM persona WHERE id_persona = %s"
                    id= input("Introduzca ID: ")
                    valor = (tuple(id),)
                    cursor.execute(sentencia,valor)
                    print("Registro Borrado")
        except Exception as e:
            print(f'Ocurrio un error {e}')
    if opcion == 5:
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = "DELETE FROM persona"
                    cursor.execute(sentencia)
                    print("Base de Datos Eliminada")
        except Exception as e:
            print(f'Ocurrio un error {e}')
    if opcion == 6:
        cursor.close()
        break;
