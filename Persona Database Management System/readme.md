# 📋 Persona Database Management System 🗃️

Este es un programa Python que permite interactuar con una base de datos PostgreSQL para gestionar registros de personas. 👥💾

## 🔍 Descripción

El programa ofrece un menú interactivo con las siguientes funcionalidades:
1. ➕ Agregar nuevas personas a la base de datos
2. 👀 Mostrar todos los registros existentes
3. 🔎 Buscar personas por su ID
4. ❌ Eliminar registros individuales
5. 💥 Eliminar todos los registros de la base de datos
6. 🚪 Salir del programa

## ⚙️ Requisitos

Para ejecutar este programa necesitas:
- 🐍 Python 3.x
- 🐘 PostgreSQL instalado y en ejecución
- 📦 La biblioteca psycopg2 (conector PostgreSQL para Python)

## 🛠️ Instalación

1. Clona este repositorio:
   ```bash
   git clone [URL del repositorio]
   ```

2. Instala las dependencias:
   ```bash
   pip install psycopg2
   ```

3. Configura la base de datos:
   - ✅ Asegúrate de tener PostgreSQL instalado y funcionando
   - 🆕 Crea una base de datos llamada 'Persona'
   - 📊 Crea una tabla con la siguiente estructura:
     ```sql
     CREATE TABLE persona (
         id_persona SERIAL PRIMARY KEY,
         nombre VARCHAR(50),
         apellido VARCHAR(50),
         email VARCHAR(100)
     );
     ```

4. ⚙️ Configura las credenciales de conexión en el código:
   ```python
   conexion = psycopg2.connect(
       user='postgres',
       password='admin',
       host='127.0.0.1',
       port='5432',
       database='Persona'
   )
   ```
   (🔐 Ajusta estos valores según tu configuración de PostgreSQL)

## 🖥️ Uso

Ejecuta el programa con:
```bash
python nombre_del_archivo.py
```

Sigue las instrucciones en el menú para realizar las operaciones deseadas. 🧭

## ⚠️ Notas importantes

- 🎓 Este programa está diseñado como demostración educativa.
- 🚨 La opción 5 eliminará TODOS los registros de la tabla persona.
- 🔒 Asegúrate de tener permisos adecuados en la base de datos.
- 💾 Se recomienda hacer copias de seguridad antes de realizar operaciones de eliminación.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request con tus mejoras. ✨

## 📜 Licencia

[MIT License](LICENSE)
