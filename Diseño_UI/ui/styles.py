APP_STYLE = """
* {
    font-family: "Segoe UI";
}

QMainWindow, QWidget {
    background: #f4f6f8;
    color: #20252b;
}

QLineEdit, QComboBox, QSpinBox {
    background: white;
    border: 1px solid #d7dce1;
    border-radius: 8px;
    padding: 9px 11px;
    min-height: 20px;
}

QLineEdit:focus, QComboBox:focus, QSpinBox:focus {
    border: 1px solid #4f7cff;
}

QPushButton {
    border: none;
    border-radius: 8px;
    padding: 10px 16px;
    background: #2f6fed;
    color: white;
    font-weight: 600;
}

QPushButton:hover {
    background: #245dcc;
}

QPushButton:pressed {
    background: #1e4fae;
}

QCheckBox {
    spacing: 8px;
}

QTableWidget {
    background: white;
    border: 1px solid #e1e5e9;
    border-radius: 8px;
    gridline-color: #edf0f2;
}

QHeaderView::section {
    background: #f7f8fa;
    border: none;
    border-bottom: 1px solid #e1e5e9;
    padding: 9px;
    font-weight: 600;
}

QScrollArea {
    border: none;
}

QFrame#card {
    background: white;
    border: 1px solid #e2e6ea;
    border-radius: 12px;
}

QFrame#sidebar {
    background: #ffffff;
    border-right: 1px solid #e2e6ea;
}

QLabel#title {
    font-size: 22px;
    font-weight: 700;
}

QLabel#subtitle {
    color: #68717c;
    font-size: 13px;
}

QLabel#sectionTitle {
    font-size: 17px;
    font-weight: 700;
}

QLabel#statusAvailable {
    color: #1b7f45;
    font-weight: 600;
}

QLabel#statusUnavailable {
    color: #c33b3b;
    font-weight: 600;
}

QPushButton#navButton {
    text-align: left;
    background: transparent;
    color: #4e5660;
    padding: 12px 16px;
    font-weight: 600;
}

QPushButton#navButton:hover {
    background: #eef3ff;
    color: #2f6fed;
}

QPushButton#navButtonActive {
    text-align: left;
    background: #eaf0ff;
    color: #2f6fed;
    padding: 12px 16px;
    font-weight: 700;
}
"""
