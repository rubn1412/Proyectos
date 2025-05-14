Herramienta de automatización en Python que obtiene datos bursátiles y envía informes por email automáticamente.

🌟 Características
Obtiene datos históricos de acciones usando Yahoo Finance

Calcula métricas clave (precio máximo, mínimo y promedio)

Automatiza la redacción de emails en Gmail

Compatible con Windows y macOS

Transferencia segura de datos usando portapapeles

📦 Requisitos
bash
pip install yfinance pyautogui pyperclip webbrowser  
🛠 Configuración
Clona el repositorio:

bash
git clone https://github.com/tuusuario/informe-acciones.git  
cd informe-acciones  
Instala las dependencias:

bash
pip install -r requirements.txt  
🖥 Cómo Usarlo
Ejecuta el script:

bash
python informe_acciones.py  
El programa solicitará:

Correo electrónico del destinatario

Asunto del email

Ticker de la acción (ej: AAPL para Apple)

Período de tiempo (ej: "1mo" para 1 mes)

Cuerpo del mensaje

⚠️ Importante:

Debes tener sesión iniciada en Gmail en tu navegador

El script contiene coordenadas de clic (ajústalas según tu resolución pantalla)

🛠 Personalización
Para ajustar las coordenadas del mouse (PyAutoGUI):

Ejecuta calibrar_posiciones.py

Mueve el mouse a los elementos y registra las coordenadas

📊 Ejemplo de Salida
El email generado incluirá:

Acción evaluada: AAPL  

Valor Máximo: USD 175.00  
Valor Mínimo: USD 165.50  
Valor Promedio: USD 170.25  
⚠️ Limitaciones
Requiere pantalla con resolución 1920x1080 (ajustar coordenadas para otras resoluciones)

Solo funciona con Gmail en el navegador predeterminado

🤝 ¿Cómo Contribuir?
Haz fork del proyecto

Crea una rama (git checkout -b mejora/feature)

Haz commit de tus cambios (git commit -m 'Agregar feature')

Haz push a la rama (git push origin mejora/feature)

Abre un Pull Request

📜 Licencia
MIT © 2023 [Tu Nombre]
