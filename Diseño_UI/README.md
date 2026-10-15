# Sistema de Restaurantes — Interfaz Desktop

Implementación inicial de la capa de interfaz (UI) basada en el diseño UX/UI entregado por el equipo.

## Tecnología

- Python
- PySide6
- Aplicación de escritorio (desktop)

## Alcance de esta implementación

Esta versión contiene únicamente la interfaz y comportamientos demostrativos necesarios para visualizar:

1. Login
2. Dashboard administrativo de Raciones
3. Menú del Comensal

La autenticación, persistencia de datos, base de datos y reglas de negocio deben ser integradas posteriormente por la capa de lógica.

## Instalación

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activarlo en Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar:

```bash
python main.py
```

## Integración con la lógica

La UI está separada en:

- `ui/login_window.py`
- `ui/admin_dashboard.py`
- `ui/menu_comensal.py`
- `ui/styles.py`

Los métodos marcados como `demo`, `placeholder` o comentarios de integración son puntos donde la lógica real puede conectarse posteriormente.
