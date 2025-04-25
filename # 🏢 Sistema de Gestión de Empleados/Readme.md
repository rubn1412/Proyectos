# 🏢 Sistema de Gestión de Empleados

Un programa en Python para administrar empleados y departamentos en una empresa, con estadísticas de personal.

## 🛠️ Tecnologías
- Python 3.x
- POO (Programación Orientada a Objetos)
- Manejo de clases, propiedades y métodos estáticos

## 📂 Estructura del Proyecto
.
├── Empleado.py # Clase Empleado (atributos y contadores)
├── Empresa.py # Clase Empresa (gestión de empleados)
├── Main.py # Menú interactivo
└── README.md # Este archivo


## 🧩 Funcionalidades
1. **Contratar empleados**  
   - Registra nombre y departamento (Finanzas/Informática)
2. **Mostrar total de empleados**  
   - Contador global de empleados registrados
3. **Estadísticas por departamento**  
   - Conteo de empleados en Finanzas vs. Informática
4. **Persistencia en memoria**  
   - Lista de empleados activos durante la ejecución

## 🚀 Cómo Ejecutar
1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/gestion-empleados.git
   cd gestion-empleados
Ejecuta el programa:

bash
python Main.py
Usa el menú interactivo:

1. Contratar Empleados
2. Total Empleados
3. Empleados por departamento
4. Salir
📝 Notas Técnicas
Usa @property para getters/setters

Implementa métodos de clase (@classmethod)

Validación básica de departamentos
