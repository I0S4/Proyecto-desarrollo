# Menú app scaffold

Este PR añade un scaffold para una pequeña app Flask que muestra los menús de los restaurantes y permite un login demo.

Credenciales demo:
- Usuario: xyz
- Contraseña: 123

Cómo ejecutar (local):

1. Crear un entorno virtual (recomendado): python -m venv venv && .\venv\Scripts\Activate.ps1
2. Instalar dependencias: python -m pip install -r requirements.txt
3. Ejecutar: python app.py
4. Abrir: http://127.0.0.1:5000 (serás redirigido a /login)

Notas:
- Las imágenes usadas en los ejemplos se cargan desde los mockups ya presentes en `Diseño Externo/Mockup` en la rama `main`.
- Si prefieres que copie físicamente los assets dentro de `static/assets/` para que la app funcione completamente offline, puedo hacerlo en un siguiente commit.
