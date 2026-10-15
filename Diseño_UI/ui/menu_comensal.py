from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
    QScrollArea,
    QGridLayout,
    QFrame,
)


class MenuComensal(QWidget):
    def __init__(self, login_window=None):
        super().__init__()

        self.login_window = login_window

        self.setWindowTitle("Sistema de Restaurantes")
        self.resize(1200, 720)

        self._build_ui()

    def _build_ui(self):
        # =========================================================
        # CONTENEDOR PRINCIPAL
        # =========================================================
        main = QVBoxLayout(self)
        main.setContentsMargins(0, 0, 0, 0)
        main.setSpacing(0)

        # =========================================================
        # BARRA SUPERIOR
        # =========================================================
        topbar = QWidget()
        topbar.setObjectName("topbar")

        top_layout = QHBoxLayout(topbar)
        top_layout.setContentsMargins(25, 15, 25, 15)

        title = QLabel("Sistema de Restaurantes")
        title.setObjectName("topTitle")

        top_layout.addWidget(title)
        top_layout.addStretch()

        user_label = QLabel("MECHE")
        user_label.setObjectName("topOption")

        campus_label = QLabel("Veli FIIS")
        campus_label.setObjectName("topOption")

        mode_label = QLabel("Todo Light")
        mode_label.setObjectName("topOption")

        top_layout.addWidget(user_label)
        top_layout.addWidget(campus_label)
        top_layout.addWidget(mode_label)

        main.addWidget(topbar)

        # =========================================================
        # CUERPO
        # =========================================================
        body = QHBoxLayout()
        body.setContentsMargins(0, 0, 0, 0)
        body.setSpacing(0)

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

        side_title = QLabel("Sistema de\nRestaurantes")
        side_title.setObjectName("sidebarTitle")
        side_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        side.addWidget(logo)
        side.addWidget(side_title)
        side.addSpacing(20)

        btn_raciones = QPushButton("Raciones")
        btn_catalogos = QPushButton("Catálogos")
        btn_maestro = QPushButton("Maestro de Platos")

        for button in (
            btn_raciones,
            btn_catalogos,
            btn_maestro,
        ):
            button.setObjectName("sidebarButton")
            side.addWidget(button)

        side.addStretch()

        btn_logout = QPushButton("Cerrar Sesión")
        btn_logout.setObjectName("sidebarButton")
        btn_logout.clicked.connect(self.logout)

        side.addWidget(btn_logout)

        # IMPORTANTE:
        # Agregamos el QWidget, no el QVBoxLayout.
        body.addWidget(side_widget)

        # =========================================================
        # CONTENIDO
        # =========================================================
        content = QWidget()

        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(30, 25, 30, 25)
        content_layout.setSpacing(18)

        # =========================================================
        # BUSCADOR
        # =========================================================
        search = QLineEdit()
        search.setPlaceholderText("Buscar plato")
        search.setObjectName("searchBox")

        content_layout.addWidget(search)

        # =========================================================
        # FILTROS
        # =========================================================
        filters = QHBoxLayout()

        category_label = QLabel("CATEGORÍA:")
        category_label.setObjectName("filterLabel")

        category_combo = QComboBox()
        category_combo.addItems(
            [
                "Entradas",
                "Segundo",
                "Postres y Bebidas",
            ]
        )

        menu_label = QLabel("TIPO DE MENÚ:")
        menu_label.setObjectName("filterLabel")

        menu_combo = QComboBox()
        menu_combo.addItems(
            [
                "Económico",
                "Universitario",
                "Ejecutivo",
            ]
        )

        filters.addWidget(category_label)
        filters.addWidget(category_combo)
        filters.addSpacing(20)
        filters.addWidget(menu_label)
        filters.addWidget(menu_combo)
        filters.addStretch()

        content_layout.addLayout(filters)

        # =========================================================
        # TÍTULO
        # =========================================================
        menu_title = QLabel("Menú Universitario")
        menu_title.setObjectName("pageTitle")

        content_layout.addWidget(menu_title)

        # =========================================================
        # ÁREA DE PLATOS
        # =========================================================
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)

        cards_container = QWidget()

        cards_layout = QGridLayout(cards_container)
        cards_layout.setContentsMargins(5, 5, 5, 5)
        cards_layout.setSpacing(18)

        # =========================================================
        # PLATOS DEL DISEÑO
        # =========================================================
        dishes = [
            ("Papa a la huancaina", "S/2.00", "Disponible"),
            ("Tequeños", "S/1.00", "Agotado"),
            ("Sopa", "S/1.00", "Disponible"),
            ("Ensalada", "S/1.00", "Disponible"),
            ("Lomo Saltado", "S/14.00", "Disponible"),
            ("Aji de Gallina", "S/10.00", "Disponible"),
            ("Arroz con pollo", "S/12.00", "Disponible"),
            ("Chicharrón de pota", "S/10.00", "Agotado"),
        ]

        for index, (name, price, status) in enumerate(dishes):
            card = self.create_dish_card(
                name,
                price,
                status,
            )

            row = index // 4
            column = index % 4

            cards_layout.addWidget(
                card,
                row,
                column,
            )

        scroll.setWidget(cards_container)

        content_layout.addWidget(scroll)

        body.addWidget(content)

        # =========================================================
        # AGREGAR CUERPO
        # =========================================================
        main.addLayout(body)

    # =============================================================
    # CREAR TARJETA DE PLATO
    # =============================================================
    def create_dish_card(
        self,
        name,
        price,
        status,
    ):
        card = QFrame()
        card.setObjectName("dishCard")

        layout = QVBoxLayout(card)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(8)

        # Imagen provisional
        image = QLabel("🍽️")
        image.setObjectName("dishImage")
        image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(image)

        # Nombre
        name_label = QLabel(name)
        name_label.setObjectName("dishName")
        name_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        name_label.setWordWrap(True)

        layout.addWidget(name_label)

        # Precio
        price_label = QLabel(price)
        price_label.setObjectName("dishPrice")
        price_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(price_label)

        # Estado
        status_label = QLabel(status)
        status_label.setObjectName(
            "availableStatus"
            if status == "Disponible"
            else "soldOutStatus"
        )

        status_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(status_label)

        return card

    # =============================================================
    # CERRAR SESIÓN
    # =============================================================
    def logout(self):
        self.close()

        if self.login_window:
            self.login_window.show()