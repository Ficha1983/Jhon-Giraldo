
# Django Project with Database Connections

Este es un proyecto Django con conexiones a bases de datos MySQL, PostgreSQL y MongoDB.

## Instalación

1. Clona o descarga el proyecto.
2. Crea un entorno virtual:
   ```bash
   python -m venv venv
   ```
3. Activa el entorno virtual:
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Mac/Linux:
     ```bash
     source venv/bin/activate
     ```
4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
5. Realiza las migraciones:
   ```bash
   python manage.py migrate
   ```
6. Ejecuta el servidor:
   ```bash
   python manage.py runserver
   ```
7. Para las bases de datos:
   - **MySQL**: Instala MySQL y crea una base de datos llamada `mydb`.
   - **PostgreSQL**: Instala PostgreSQL y crea una base de datos llamada `mydb`.
   - **MongoDB**: Instala MongoDB y asegúrate de que esté corriendo en el puerto 27017.
   