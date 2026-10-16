"""Launcher para la aplicación "Sistema de Restaurantes" (demo)

Este script carga la interfaz gráfica que ya existe en Diseño_UI/ui y aplica
los estilos definidos en ui/styles.py. Para evitar problemas con el nombre
con caracteres especiales de la carpeta ("Diseño_UI"), el script añade
esa carpeta al sys.path y luego importa el paquete `ui`.

Instrucciones rápidas:
1. Instala dependencias: pip install -r requirements.txt
2. Ejecuta: python run_app.py
"""

import sys
import os

# Añadimos la carpeta Diseño_UI al sys.path para poder importar el paquete `ui`
BASE_DIR = os.path.dirname(__file__)
DISENO_DIR = os.path.join(BASE_DIR, "Diseño_UI")
if DISENO_DIR not in sys.path:
    sys.path.insert(0, DISENO_DIR)

from PySide6.QtWidgets import QApplication

# importamos estilos y ventana de login desde el paquete `ui`
from ui.styles import APP_STYLE
from ui.login_window import LoginWindow


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(APP_STYLE)

    window = LoginWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
