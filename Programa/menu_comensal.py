from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QLineEdit, QComboBox, QScrollArea, QGridLayout, QFrame,
    QStackedWidget, QTableWidget, QTableWidgetItem, QHeaderView
)

class MenuComensal(QWidget):
    def __init__(self, login_window=None, shared_db=None):
        super().__init__()
        self.login_window = login_window
        
        if shared_db is not None:
            self.shared_db = shared_db
        else:
            self.shared_db = {"MECHE": [], "Veli FIIS": [], "Todo Light": []}

        self.setWindowTitle("Sistema de Restaurantes - Vista Comensal")
        self.resize(1200, 720)
        self._build_ui()
        self.actualizar_vistas()

    def _build_ui(self):
        main = QVBoxLayout(self)
        main.setContentsMargins(0, 0, 0, 0)
        main.setSpacing(0)

        # ==================== BARRA SUPERIOR ====================
        topbar = QWidget()
        topbar.setObjectName("topbar")
        top_layout = QHBoxLayout(topbar)
        top_layout.setContentsMargins(25, 15, 25, 15)

        title = QLabel("Sistema de Restaurantes")
        title.setObjectName("topTitle")
        top_layout.addWidget(title)
        top_layout.addStretch()

        self.restaurante_combo = QComboBox()
        self.restaurante_combo.addItems(["MECHE", "Veli FIIS", "Todo Light"])
        top_layout.addWidget(QLabel("Restaurante:"))
        top_layout.addWidget(self.restaurante_combo)
        
        main.addWidget(topbar)

        # ==================== CUERPO ====================
        body = QHBoxLayout()
        body.setContentsMargins(0, 0, 0, 0)
        body.setSpacing(0)

        # ==================== BARRA LATERAL ====================
        side_widget = QWidget()
        side_widget.setObjectName("sidebar")
        side = QVBoxLayout(side_widget)
        side.setContentsMargins(20, 25, 20, 20)
        side.setSpacing(12)

        logo = QLabel("🍽️")
        logo.setObjectName("logo")
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        side.addWidget(logo)
        
        side_title = QLabel("Sistema de\nRestaurantes")
        side_title.setObjectName("sidebarTitle")
        side_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        side.addWidget(side_title)
        side.addSpacing(20)

        # Botones de navegación funcionales
        btn_raciones = QPushButton("Raciones")
        btn_raciones.setObjectName("sidebarButton")
        btn_raciones.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        side.addWidget(btn_raciones)

        btn_catalogos = QPushButton("Catálogos")
        btn_catalogos.setObjectName("sidebarButton")
        btn_catalogos.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        side.addWidget(btn_catalogos)

        btn_maestro = QPushButton("Maestro de Platos")
        btn_maestro.setObjectName("sidebarButton")
        btn_maestro.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        side.addWidget(btn_maestro)

        side.addStretch()
        btn_logout = QPushButton("Volver al Inicio")
        btn_logout.setObjectName("sidebarButton")
        btn_logout.clicked.connect(self.logout)
        side.addWidget(btn_logout)
        
        body.addWidget(side_widget)

        # ==================== CONTENEDOR DE PANTALLAS (STACK) ====================
        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(30, 25, 30, 25)
        
        self.stacked_widget = QStackedWidget()
        content_layout.addWidget(self.stacked_widget)
        
        # --- PANTALLA 1: RACIONES (Índice 0) ---
        page_raciones = QWidget()
        layout_raciones = QVBoxLayout(page_raciones)
        title_raciones = QLabel("Estado de Raciones del Restaurante")
        title_raciones.setObjectName("pageTitle")
        layout_raciones.addWidget(title_raciones)
        
        self.table_raciones = QTableWidget(0, 5)
        self.table_raciones.setHorizontalHeaderLabels(["RESTAURANTE", "PLATILLO", "CATEGORÍA", "RACIONES", "ESTADO"])
        self.table_raciones.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table_raciones.setAlternatingRowColors(True)
        self.table_raciones.setSelectionMode(QTableWidget.SelectionMode.NoSelection) # Solo lectura
        layout_raciones.addWidget(self.table_raciones)
        
        self.stacked_widget.addWidget(page_raciones)

        # --- PANTALLA 2: CATÁLOGOS (Índice 1) ---
        page_catalogos = QWidget()
        layout_catalogos = QVBoxLayout(page_catalogos)
        title_catalogos = QLabel("Catálogo Maestro de Precios")
        title_catalogos.setObjectName("pageTitle")
        layout_catalogos.addWidget(title_catalogos)
        
        self.table_catalogos = QTableWidget(3, 3)
        self.table_catalogos.setHorizontalHeaderLabels(["Código Categoría", "Nombre Categoría", "Rango Precio"])
        self.table_catalogos.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table_catalogos.setAlternatingRowColors(True)
        self.table_catalogos.setSelectionMode(QTableWidget.SelectionMode.NoSelection)
        
        # Llenar la tabla de catálogos estática
        cat_data = [
            ["C001", "Económico", "<0-10]"],
            ["C002", "Universitario", "<10-12]"],
            ["C003", "Ejecutivo", "<12-20]"]
        ]
        for row, row_data in enumerate(cat_data):
            for col, val in enumerate(row_data):
                item = QTableWidgetItem(val)
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.table_catalogos.setItem(row, col, item)
                
        layout_catalogos.addWidget(self.table_catalogos)
        layout_catalogos.addStretch()
        self.stacked_widget.addWidget(page_catalogos)

        # --- PANTALLA 3: MAESTRO DE PLATOS (Índice 2) ---
        page_maestro = QWidget()
        layout_maestro = QVBoxLayout(page_maestro)
        layout_maestro.setSpacing(18)

        self.search = QLineEdit()
        self.search.setPlaceholderText("Buscar plato...")
        self.search.setObjectName("searchBox")
        layout_maestro.addWidget(self.search)

        filters = QHBoxLayout()
        self.category_combo = QComboBox()
        self.category_combo.addItems(["Todas", "Entradas", "Segundo", "Postres y Bebidas"])
        
        self.menu_combo = QComboBox()
        self.menu_combo.addItems(["Todos", "Económico", "Universitario", "Ejecutivo"])

        filters.addWidget(QLabel("CATEGORÍA:"))
        filters.addWidget(self.category_combo)
        filters.addSpacing(20)
        filters.addWidget(QLabel("TIPO DE MENÚ:"))
        filters.addWidget(self.menu_combo)
        filters.addStretch()
        layout_maestro.addLayout(filters)

        self.menu_title = QLabel("Menú Disponible")
        self.menu_title.setObjectName("pageTitle")
        layout_maestro.addWidget(self.menu_title)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)

        self.cards_container = QWidget()
        self.cards_layout = QGridLayout(self.cards_container)
        self.cards_layout.setContentsMargins(5, 5, 5, 5)
        self.cards_layout.setSpacing(18)
        
        scroll.setWidget(self.cards_container)
        layout_maestro.addWidget(scroll)
        
        self.stacked_widget.addWidget(page_maestro)

        # Configurar pantalla inicial en "Maestro de Platos" (Índice 2)
        self.stacked_widget.setCurrentIndex(2)

        body.addWidget(content)
        main.addLayout(body)

        # ==================== EVENTOS ====================
        self.restaurante_combo.currentTextChanged.connect(self.actualizar_vistas)
        self.search.textChanged.connect(self.actualizar_vistas)
        self.category_combo.currentTextChanged.connect(self.actualizar_vistas)
        self.menu_combo.currentTextChanged.connect(self.actualizar_vistas)

    def actualizar_vistas(self):
        # 1. Actualizar la tabla de raciones
        self.table_raciones.setRowCount(0)
        restaurante_actual = self.restaurante_combo.currentText()
        platos = self.shared_db.get(restaurante_actual, [])
        
        for plato in platos:
            row = self.table_raciones.rowCount()
            self.table_raciones.insertRow(row)
            datos = [restaurante_actual, plato["nombre"], plato["categoria"], plato.get("raciones", "N/A"), plato["estado"]]
            for col, val in enumerate(datos):
                item = QTableWidgetItem(str(val))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.table_raciones.setItem(row, col, item)

        # 2. Actualizar las tarjetas del Maestro de Platos
        for i in reversed(range(self.cards_layout.count())): 
            widget = self.cards_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        texto_busqueda = self.search.text().lower()
        categoria_actual = self.category_combo.currentText()
        tipo_actual = self.menu_combo.currentText()
        platos_filtrados = []

        for plato in platos:
            coincide_texto = texto_busqueda in plato["nombre"].lower()
            coincide_categoria = categoria_actual == "Todas" or plato["categoria"] == categoria_actual
            coincide_tipo = tipo_actual == "Todos" or plato["tipo"] == tipo_actual

            if coincide_texto and coincide_categoria and coincide_tipo:
                platos_filtrados.append(plato)

        for index, plato in enumerate(platos_filtrados):
            card = self.create_dish_card(plato["nombre"], plato["precio"], plato["estado"], plato.get("raciones", "N/A"))
            row = index // 4
            column = index % 4
            self.cards_layout.addWidget(card, row, column)

    def create_dish_card(self, name, price, status, raciones):
        card = QFrame()
        card.setObjectName("dishCard")
        layout = QVBoxLayout(card)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(8)

        image = QLabel("🍽️")
        image.setObjectName("dishImage")
        image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(image)

        name_label = QLabel(name)
        name_label.setObjectName("dishName")
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name_label.setWordWrap(True)
        layout.addWidget(name_label)

        price_label = QLabel(price)
        price_label.setObjectName("dishPrice")
        price_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(price_label)
        
        raciones_label = QLabel(f"Raciones: {raciones}")
        raciones_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(raciones_label)

        status_label = QLabel(status)
        status_label.setObjectName("availableStatus" if status == "Disponible" else "soldOutStatus")
        status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(status_label)

        return card

    def logout(self):
        self.close()
        if self.login_window:
            self.login_window.show()

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    try:
        from styles import APP_STYLE
        app.setStyleSheet(APP_STYLE)
    except ImportError:
        pass
        
    ventana = MenuComensal()
    ventana.show()
    sys.exit(app.exec())