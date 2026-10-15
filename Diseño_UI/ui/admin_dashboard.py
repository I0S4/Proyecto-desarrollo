from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
    QSpinBox,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QMessageBox,
)


class AdminDashboard(QWidget):
    def __init__(self, login_window=None):
        super().__init__()
        self.login_window = login_window

        self.setWindowTitle("Sistema de Restaurantes - Módulo Administrativo")
        self.resize(1200, 720)

        self._build_ui()

    def _build_ui(self):
        # =========================================================
        # CONTENEDOR PRINCIPAL
        # =========================================================
        main = QHBoxLayout(self)
        main.setContentsMargins(0, 0, 0, 0)
        main.setSpacing(0)

        # =========================================================
        # SIDEBAR
        # =========================================================
        side_widget = QWidget()
        side_widget.setObjectName("sidebar")

        side = QVBoxLayout(side_widget)
        side.setContentsMargins(20, 25, 20, 20)
        side.setSpacing(12)

        logo = QLabel("🍽️")
        logo.setObjectName("logo")
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title = QLabel("Sistema de\nRestaurantes")
        title.setObjectName("sidebarTitle")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        side.addWidget(logo)
        side.addWidget(title)
        side.addSpacing(25)

        btn_raciones = QPushButton("Raciones")
        btn_catalogos = QPushButton("Catálogos")
        btn_maestro = QPushButton("Maestro de Platos")

        for button in (btn_raciones, btn_catalogos, btn_maestro):
            button.setObjectName("sidebarButton")
            side.addWidget(button)

        side.addStretch()

        btn_logout = QPushButton("Cerrar Sesión")
        btn_logout.setObjectName("sidebarButton")
        btn_logout.clicked.connect(self.logout)

        side.addWidget(btn_logout)

        # IMPORTANTE:
        # side_widget es un QWidget, por eso sí puede utilizarse
        # con addWidget().
        main.addWidget(side_widget)

        # =========================================================
        # CONTENIDO PRINCIPAL
        # =========================================================
        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(30, 25, 30, 25)
        content_layout.setSpacing(18)

        # Título
        header = QLabel(
            "Estado de Raciones y Stock en Tiempo Real"
        )
        header.setObjectName("pageTitle")

        content_layout.addWidget(header)

        # =========================================================
        # FORMULARIO
        # =========================================================
        form_box = QWidget()
        form_layout = QVBoxLayout(form_box)
        form_layout.setContentsMargins(20, 20, 20, 20)
        form_layout.setSpacing(12)

        form_title = QLabel("Registrar Raciones del Día")
        form_title.setObjectName("sectionTitle")

        form_layout.addWidget(form_title)

        row1 = QHBoxLayout()

        # Tipo
        type_layout = QVBoxLayout()

        type_label = QLabel("Entrada / Segundo")
        self.type_combo = QComboBox()
        self.type_combo.addItems(["Entrada", "Segundo"])

        type_layout.addWidget(type_label)
        type_layout.addWidget(self.type_combo)

        # Platillo
        dish_layout = QVBoxLayout()

        dish_label = QLabel("Seleccionar Platillo")
        self.dish_combo = QComboBox()
        self.dish_combo.addItems(
            [
                "Tequeños",
                "Arroz con Pollo",
                "Pollo al Horno",
                "Lomo Saltado",
                "Ají de Gallina",
            ]
        )

        dish_layout.addWidget(dish_label)
        dish_layout.addWidget(self.dish_combo)

        # Raciones
        quantity_layout = QVBoxLayout()

        quantity_label = QLabel("Número de Raciones")

        self.quantity_spin = QSpinBox()
        self.quantity_spin.setMinimum(0)
        self.quantity_spin.setMaximum(9999)
        self.quantity_spin.setValue(10)

        quantity_layout.addWidget(quantity_label)
        quantity_layout.addWidget(self.quantity_spin)

        row1.addLayout(type_layout)
        row1.addLayout(dish_layout)
        row1.addLayout(quantity_layout)

        form_layout.addLayout(row1)

        btn_save = QPushButton("+  Guardar Raciones")
        btn_save.setObjectName("primaryButton")
        btn_save.clicked.connect(self.save_rations)

        form_layout.addWidget(
            btn_save,
            alignment=Qt.AlignmentFlag.AlignLeft
        )

        content_layout.addWidget(form_box)

        # =========================================================
        # TABLA
        # =========================================================
        table_title = QLabel("Raciones registradas")
        table_title.setObjectName("sectionTitle")

        content_layout.addWidget(table_title)

        self.table = QTableWidget(0, 6)

        self.table.setHorizontalHeaderLabels(
            [
                "CÓDIGO",
                "PLATILLO",
                "TIPO",
                "RACIONES",
                "PRECIO",
                "ESTADO",
            ]
        )

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )

        content_layout.addWidget(self.table)

        # Datos de ejemplo del diseño
        self.add_row(
            "ENT-01",
            "Tequeños",
            "Entrada",
            "18",
            "S/4.00",
            "Disponible",
        )

        self.add_row(
            "SEG-01",
            "Arroz con Pollo",
            "Segundo",
            "0",
            "S/10.00",
            "Agotado",
        )

        self.add_row(
            "SEG-02",
            "Pollo al Horno",
            "Segundo",
            "25",
            "S/12.00",
            "Disponible",
        )

        # Editar parámetros
        edit_button = QPushButton("Editar parámetros")
        edit_button.setObjectName("secondaryButton")

        content_layout.addWidget(
            edit_button,
            alignment=Qt.AlignmentFlag.AlignRight
        )

        main.addWidget(content)

    # =============================================================
    # AGREGAR FILA A LA TABLA
    # =============================================================
    def add_row(
        self,
        code,
        dish,
        dish_type,
        quantity,
        price,
        status,
    ):
        row = self.table.rowCount()
        self.table.insertRow(row)

        values = [
            code,
            dish,
            dish_type,
            quantity,
            price,
            status,
        ]

        for column, value in enumerate(values):
            self.table.setItem(
                row,
                column,
                QTableWidgetItem(str(value))
            )

    # =============================================================
    # GUARDAR RACIONES
    # =============================================================
    def save_rations(self):
        dish = self.dish_combo.currentText()
        dish_type = self.type_combo.currentText()
        quantity = self.quantity_spin.value()

        if dish_type == "Entrada":
            code = "ENT-NEW"
            price = "S/4.00"
        else:
            code = "SEG-NEW"
            price = "S/10.00"

        status = (
            "Disponible"
            if quantity > 0
            else "Agotado"
        )

        self.add_row(
            code,
            dish,
            dish_type,
            str(quantity),
            price,
            status,
        )

        QMessageBox.information(
            self,
            "Raciones",
            "Las raciones fueron registradas correctamente."
        )

    # =============================================================
    # CERRAR SESIÓN
    # =============================================================
    def logout(self):
        self.close()

        if self.login_window:
            self.login_window.show()