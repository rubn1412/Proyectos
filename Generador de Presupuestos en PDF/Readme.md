Aplicación Python para generar presupuestos automáticos en formato PDF.

## 🚀 Características

- Genera presupuestos profesionales en PDF
- Configuración personalizada de horas y tarifas
- Plantilla editable para diseño personalizado
- Fácil integración con otros sistemas

## 📦 Requisitos

- Python 3.8+
- Biblioteca FPDF (`pip install fpdf`)

## 🛠 Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/generador-presupuestos.git
   cd generador-presupuestos
Instala las dependencias:

bash
pip install fpdf
Prepara tu plantilla:

Coloca tu imagen Template.png en la misma carpeta

Ajusta las coordenadas en el código según tu plantilla

🖥 Uso
Ejecuta el programa:

bash
python presupuesto.py
El programa solicitará:

Nombre del proyecto

Horas estimadas por día

Duración del proyecto (en días)

Precio por hora

Generará un archivo Presupuesto.pdf con los datos ingresados.

🎚 Personalización
Para ajustar las posiciones del texto:

python
pdf.text(x, y, texto)  # Ajusta x, y según tu plantilla
📄 Estructura del Proyecto
generador-presupuestos/
├── presupuesto.py      # Script principal
├── Template.png        # Plantilla del presupuesto
├── Presupuesto.pdf     # Ejemplo de salida
└── README.md           # Este archivo
🤝 Contribución
Las contribuciones son bienvenidas. Por favor abre un Issue o Pull Request.

📜 Licencia
MIT
