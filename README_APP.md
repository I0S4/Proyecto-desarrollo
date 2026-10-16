Sistema de Restaurantes - Demo (UNI)

Esta carpeta contiene una interfaz gráfica de ejemplo que muestra los menús
de los restaurantes (diseñada para la UNI). Los archivos de interfaz están
bajo la carpeta `Diseño_UI/ui`.

Archivos añadidos:
- run_app.py: lanzador que carga la GUI desde `Diseño_UI/ui`.
- requirements.txt: dependencias mínimas.

Cómo ejecutar (entorno Python 3.8+):

1) Crear y activar un entorno virtual (opcional pero recomendado):

   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate

2) Instalar dependencias:

   pip install -r requirements.txt

3) Ejecutar la aplicación:

   python run_app.py

Notas:
- La demo usa PySide6 y las pantallas ya implementadas en `Diseño_UI/ui`.
- Si tu sistema no soporta bien nombres de carpetas con caracteres especiales
  (como la ñ), el launcher añade la carpeta `Diseño_UI` al PYTHONPATH y
  luego importa el paquete `ui`, por eso no se hace "import Diseño_UI.ui".
- Para integrar con una base de datos o una API real, modifica los módulos
  bajo `Diseño_UI/ui` (por ejemplo `menu_comensal.py` y `admin_dashboard.py`).
