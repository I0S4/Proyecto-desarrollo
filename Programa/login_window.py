from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QCheckBox, QFrame, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QWidget
)

from admin_dashboard import AdminDashboard
from menu_comensal import MenuComensal

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Restaurantes - Login")
        self.setMinimumSize(900, 600)
        self.resize(1100, 700)
        
        # Base de datos: Las entradas ahora dicen "Incluido"
        self.shared_db = {
            "MECHE": [
                {"nombre": "Papa a la huancaina", "precio": "Incluido", "estado": "Disponible", "categoria": "Entradas", "tipo": "Económico", "raciones": "50"},
                {"nombre": "Lomo Saltado", "precio": "S/14.00", "estado": "Disponible", "categoria": "Segundo", "tipo": "Ejecutivo", "raciones": "30"},
            ],
            "Veli FIIS": [
                {"nombre": "Arroz con pollo", "precio": "S/12.00", "estado": "Disponible", "categoria": "Segundo", "tipo": "Universitario", "raciones": "45"},
            ],
            "Todo Light": [
                {"nombre": "Ensalada César", "precio": "Incluido", "estado": "Disponible", "categoria": "Entradas", "tipo": "Ejecutivo", "raciones": "20"},
            ]
        }

        self._build_ui()

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        outer = QVBoxLayout(central)
        outer.setContentsMargins(30, 30, 30, 30)
        outer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        card = QFrame()
        card.setObjectName("card")
        card.setMaximumWidth(430)

        layout = QVBoxLayout(card)
        layout.setContentsMargins(38, 35, 38, 35)
        layout.setSpacing(14)

        logo = QLabel("🍽")
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo.setStyleSheet("font-size: 48px;")

        title = QLabel("Sistema de Restaurantes")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        subtitle = QLabel("Inicia sesión para continuar")
        subtitle.setObjectName("subtitle")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        user_label = QLabel("Usuario")
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Ingresa tu usuario")

        password_label = QLabel("Contraseña")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Ingresa tu contraseña")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.remember = QCheckBox("Recordar sesión")

        login_button = QPushButton("Iniciar Sesión")
        login_button.setMinimumHeight(44)
        login_button.clicked.connect(self.handle_login)

        demo_row = QHBoxLayout()
        admin_demo = QPushButton("Demo Administrador")
        comensal_demo = QPushButton("Demo Comensal")
        admin_demo.clicked.connect(self.open_admin)
        comensal_demo.clicked.connect(self.open_comensal)
        demo_row.addWidget(admin_demo)
        demo_row.addWidget(comensal_demo)

        layout.addWidget(logo)
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(8)
        layout.addWidget(user_label)
        layout.addWidget(self.user_input)
        layout.addWidget(password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.remember)
        layout.addSpacing(6)
        layout.addWidget(login_button)
        layout.addSpacing(4)
        layout.addLayout(demo_row)

        outer.addWidget(card)

    def handle_login(self):
        usuario = self.user_input.text().strip()
        contrasena = self.password_input.text().strip()

        if not usuario or not contrasena:
            QMessageBox.warning(self, "Datos incompletos", "Ingresa usuario y contraseña.")
            return

        if usuario == "xyz" and contrasena == "123":
            self.open_admin()
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos.")

    def open_admin(self):
        self.dashboard = AdminDashboard(self, self.shared_db)
        self.dashboard.show()
        self.hide()

    def open_comensal(self):
        self.menu = MenuComensal(self, self.shared_db)
        self.menu.show()
        self.hide()

    def show_login(self):
        self.show()
        self.raise_()
        self.activateWindow()

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    try:
        from styles import APP_STYLE
        app.setStyleSheet(APP_STYLE)
    except ImportError:
        pass
    
    ventana = LoginWindow()
    ventana.show()
    sys.exit(app.exec())
