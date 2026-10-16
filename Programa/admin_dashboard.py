from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QComboBox, QLineEdit, QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox, QGridLayout
)

class AdminDashboard(QWidget):
    def __init__(self, login_window=None, shared_db=None):
        super().__init__()
        self.login_window = login_window
        self.shared_db = shared_db if shared_db is not None else {"MECHE": [], "Veli FIIS": [], "Todo Light": []}

        # CATÁLOGO MAESTRO DE PLATOS PREDEFINIDOS Y PRECIOS FIJOS
        self.catalogo_maestro = {
            "MECHE": {
                "Entradas": [
                    {"nombre": "Tequeños (6 unid.)", "precio": "Incluido"},
                    {"nombre": "Papa a la Huancaína", "precio": "Incluido"},
                    {"nombre": "Sopa a la Minuta", "precio": "Incluido"}
                ],
                "Segundo": [
                    {"nombre": "Tallarín Rojo con Pollo", "precio": "S/10.00"},
                    {"nombre": "Hamburguesa de Lentejas c/ Ensalada", "precio": "S/10.00"},
                    {"nombre": "Ají de Gallina", "precio": "S/12.00"},
                    {"nombre": "Arroz Chaufa de Pollo", "precio": "S/13.00"},
                    {"nombre": "Lomo Saltado", "precio": "S/14.00"},
                    {"nombre": "Tallarines Verdes con Bistec", "precio": "S/15.00"}
                ],
                "Postres y Bebidas": [
                    {"nombre": "Chicha Morada (Jarra)", "precio": "S/5.00"},
                    {"nombre": "Crema Volteada", "precio": "S/4.50"}
                ]
            },
            "Veli FIIS": {
                "Entradas": [
                    {"nombre": "Causa Limeña", "precio": "Incluido"},
                    {"nombre": "Ceviche de Pota", "precio": "Incluido"},
                    {"nombre": "Ocopa Arequipeña", "precio": "Incluido"}
                ],
                "Segundo": [
                    {"nombre": "Guiso de Arvejas con Pollo", "precio": "S/10.00"},
                    {"nombre": "Estofado de Pollo", "precio": "S/11.00"},
                    {"nombre": "Arroz con Pollo", "precio": "S/12.00"},
                    {"nombre": "Pollo al Horno con Puré", "precio": "S/13.00"},
                    {"nombre": "Pescado Frito con Yuca", "precio": "S/13.00"},
                    {"nombre": "Seco de Carne con Frijoles", "precio": "S/14.00"}
                ],
                "Postres y Bebidas": [
                    {"nombre": "Refresco de Maracuyá", "precio": "S/2.50"},
                    {"nombre": "Gelatina de Fresa", "precio": "S/2.00"}
                ]
            },
            "Todo Light": {
                "Entradas": [
                    {"nombre": "Ensalada Fresca Mixta", "precio": "Incluido"},
                    {"nombre": "Crema de Zapallo", "precio": "Incluido"},
                    {"nombre": "Salpicón de Pollo", "precio": "Incluido"}
                ],
                "Segundo": [
                    {"nombre": "Quinoa Atamalada", "precio": "S/11.00"},
                    {"nombre": "Omelette de Verduras", "precio": "S/12.00"},
                    {"nombre": "Saltado de Brócoli y Pollo", "precio": "S/13.00"},
                    {"nombre": "Pechuga a la Plancha c/ Ensalada", "precio": "S/14.00"},
                    {"nombre": "Pescado al Vapor", "precio": "S/15.00"}
                ],
                "Postres y Bebidas": [
                    {"nombre": "Agua de Manzana", "precio": "S/2.00"},
                    {"nombre": "Ensalada de Frutas", "precio": "S/6.00"}
                ]
            }
        }

        self.setWindowTitle("Sistema de Restaurantes - Módulo Administrativo")
        self.resize(1200, 720)
        self._build_ui()
        self.cargar_datos_tabla()

    def _build_ui(self):
        main = QHBoxLayout(self)
        main.setContentsMargins(0, 0, 0, 0)
        main.setSpacing(0)

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

        for text in ("Raciones", "Catálogos", "Maestro de Platos"):
            btn = QPushButton(text)
            btn.setObjectName("sidebarButton")
            side.addWidget(btn)

        side.addStretch()
        btn_logout = QPushButton("Volver al Inicio")
        btn_logout.setObjectName("sidebarButton")
        btn_logout.clicked.connect(self.logout)
        side.addWidget(btn_logout)
        main.addWidget(side_widget)

        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(30, 25, 30, 25)
        content_layout.setSpacing(18)

        header = QLabel("Gestión de Menú en Tiempo Real")
        header.setObjectName("pageTitle")
        content_layout.addWidget(header)

        form_box = QWidget()
        form_layout = QGridLayout(form_box)
        form_layout.setContentsMargins(20, 20, 20, 20)
        form_layout.setSpacing(12)

        form_layout.addWidget(QLabel("Registrar Raciones del Día"), 0, 0, 1, 3)

        form_layout.addWidget(QLabel("Restaurante"), 1, 0)
        self.rest_combo = QComboBox()
        self.rest_combo.addItems(["MECHE", "Veli FIIS", "Todo Light"])
        form_layout.addWidget(self.rest_combo, 2, 0)

        form_layout.addWidget(QLabel("Entrada / Segundo"), 1, 1)
        self.cat_combo = QComboBox()
        self.cat_combo.addItems(["Entradas", "Segundo", "Postres y Bebidas"])
        form_layout.addWidget(self.cat_combo, 2, 1)

        form_layout.addWidget(QLabel("Seleccionar Platillo"), 1, 2)
        self.dish_combo = QComboBox()
        form_layout.addWidget(self.dish_combo, 2, 2)

        form_layout.addWidget(QLabel("Número de Raciones"), 3, 0)
        self.raciones_input = QLineEdit()
        self.raciones_input.setPlaceholderText("Ej. 50")
        form_layout.addWidget(self.raciones_input, 4, 0)

        form_layout.addWidget(QLabel("Estado"), 3, 1)
        self.status_combo = QComboBox()
        self.status_combo.addItems(["Disponible", "Agotado"])
        form_layout.addWidget(self.status_combo, 4, 1)

        btn_save = QPushButton("+ Guardar Raciones")
        btn_save.setObjectName("primaryButton")
        btn_save.clicked.connect(self.save_rations)
        form_layout.addWidget(btn_save, 5, 0, 1, 3, Qt.AlignmentFlag.AlignLeft)

        content_layout.addWidget(form_box)

        content_layout.addWidget(QLabel("Raciones Registradas (Todos los Restaurantes)"))
        
        self.table = QTableWidget(0, 7)
        self.table.setHorizontalHeaderLabels(["RESTAURANTE", "PLATILLO", "CATEGORÍA", "TIPO", "PRECIO", "RACIONES", "ESTADO"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        content_layout.addWidget(self.table)

        action_buttons_layout = QHBoxLayout()
        
        btn_toggle = QPushButton("Cambiar Estado (Disponible/Agotado)")
        btn_toggle.setStyleSheet("background-color: #f0ad4e; color: white; border-radius: 8px; padding: 10px 16px; font-weight: 600;")
        btn_toggle.clicked.connect(self.toggle_status)

        btn_delete = QPushButton("Eliminar selección")
        btn_delete.setStyleSheet("background-color: #d9534f; color: white; border-radius: 8px; padding: 10px 16px; font-weight: 600;")
        btn_delete.clicked.connect(self.delete_rations)

        action_buttons_layout.addWidget(btn_toggle)
        action_buttons_layout.addWidget(btn_delete)
        action_buttons_layout.addStretch()
        content_layout.addLayout(action_buttons_layout)
        main.addWidget(content)

        self.rest_combo.currentTextChanged.connect(self.actualizar_platos_combo)
        self.cat_combo.currentTextChanged.connect(self.actualizar_platos_combo)
        self.actualizar_platos_combo()

    def calcular_tipo_menu(self, precio_str):
        """Calcula automáticamente el tipo de menú según el rango de precios."""
        if precio_str == "Incluido":
            return "Económico"
        
        try:
            limpio = precio_str.replace("S/", "").strip()
            precio = float(limpio)
            
            if precio <= 10.0:
                return "Económico"
            elif 10.0 < precio <= 12.0:
                return "Universitario"
            else:
                return "Ejecutivo"
        except ValueError:
            return "Económico"

    def actualizar_platos_combo(self):
        self.dish_combo.clear()
        rest = self.rest_combo.currentText()
        cat = self.cat_combo.currentText()
        
        platos = self.catalogo_maestro.get(rest, {}).get(cat, [])
        for p in platos:
            if p['precio'] == "Incluido":
                self.dish_combo.addItem(f"{p['nombre']} (Incluido)", p)
            else:
                self.dish_combo.addItem(f"{p['nombre']} ({p['precio']})", p)

    def cargar_datos_tabla(self):
        self.table.setRowCount(0)
        for rest, platos in self.shared_db.items():
            for plato in platos:
                row = self.table.rowCount()
                self.table.insertRow(row)
                datos = [rest, plato["nombre"], plato["categoria"], plato["tipo"], plato["precio"], plato.get("raciones", "N/A"), plato["estado"]]
                for col, val in enumerate(datos):
                    item = QTableWidgetItem(str(val))
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                    self.table.setItem(row, col, item)

    def save_rations(self):
        rest = self.rest_combo.currentText()
        plato_data = self.dish_combo.currentData() 
        raciones = self.raciones_input.text().strip()
        
        if not plato_data:
            QMessageBox.warning(self, "Error", "No hay platillos disponibles para esta selección.")
            return

        if not raciones:
            raciones = "N/A"

        tipo_auto = self.calcular_tipo_menu(plato_data["precio"])

        nuevo_plato = {
            "nombre": plato_data["nombre"],
            "precio": plato_data["precio"],
            "estado": self.status_combo.currentText(),
            "categoria": self.cat_combo.currentText(),
            "tipo": tipo_auto,
            "raciones": raciones
        }

        self.shared_db[rest].append(nuevo_plato)
        self.cargar_datos_tabla()
        
        self.raciones_input.clear()
        QMessageBox.information(self, "Éxito", "Las raciones se guardaron correctamente.")

    def delete_rations(self):
        selected_items = self.table.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Atención", "Selecciona una fila para eliminar.")
            return

        respuesta = QMessageBox.question(self, "Confirmar", "¿Eliminar raciones del menú?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if respuesta == QMessageBox.StandardButton.Yes:
            rows = set(item.row() for item in selected_items)
            for row in sorted(rows, reverse=True):
                rest = self.table.item(row, 0).text()
                dish_name = self.table.item(row, 1).text()

                for plato in self.shared_db[rest]:
                    if plato["nombre"] == dish_name:
                        self.shared_db[rest].remove(plato)
                        break

            self.cargar_datos_tabla()

    def toggle_status(self):
        selected_items = self.table.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Atención", "Selecciona una fila en la tabla para cambiar su estado.")
            return

        respuesta = QMessageBox.question(
            self, "Confirmar cambio de estado", 
            "¿Estás seguro de que deseas cambiar el estado de disponibilidad de este platillo?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if respuesta == QMessageBox.StandardButton.Yes:
            rows = set(item.row() for item in selected_items)
            for row in rows:
                rest = self.table.item(row, 0).text()
                dish_name = self.table.item(row, 1).text()

                for plato in self.shared_db[rest]:
                    if plato["nombre"] == dish_name:
                        if plato["estado"] == "Disponible":
                            plato["estado"] = "Agotado"
                            plato["raciones"] = "0" 
                        else:
                            plato["estado"] = "Disponible"
                        break

            self.cargar_datos_tabla() 

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
    ventana = AdminDashboard()
    ventana.show()
    sys.exit(app.exec())
