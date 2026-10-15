import sys
from PySide6.QtWidgets import QApplication
from ui.login_window import LoginWindow
from ui.styles import APP_STYLE


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Sistema de Restaurantes")
    app.setStyleSheet(APP_STYLE)

    window = LoginWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
