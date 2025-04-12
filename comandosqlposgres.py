import psycopg2
import datetime

def imprimir_separador(titulo):
    print("\n" + "="*50)
    print(titulo)
    print("="*50)

def ejecutar_consulta(cursor, consulta):
    try:
        cursor.execute(consulta)
        print(f"Consulta ejecutada con éxito: {consulta}")
    except psycopg2.Error as e:
        print(f"Error al ejecutar la consulta: {e}")

def mostrar_resultados(cursor):
    resultados = cursor.fetchall()
    if resultados:
        for row in resultados:
            print(row)
    else:
        print("No se encontraron resultados")

# Conectar a PostgreSQL
try:
    conexion = psycopg2.connect(
        host="localhost",      # Dirección del servidor
        user="postgres",       # Usuario de PostgreSQL
        password="123.abz",       # Contraseña
        database="PostgreSQL 17",   # Base de datos por defecto
        port=5432             # Puerto de PostgreSQL
    )
    print("✅ Conexión exitosa a PostgreSQL")
    cursor = conexion.cursor()
except psycopg2.Error as e:
    print(f"Error al conectar a PostgreSQL: {e}")
    exit(1)

# 1. DDL - Comandos de Definición de Datos
imprimir_separador("1. DDL - Creación de Tablas")

# Crear tabla de categorías
ejecutar_consulta(cursor, '''
CREATE TABLE IF NOT EXISTS categorias (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Crear tabla de productos
ejecutar_consulta(cursor, '''
CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    categoria_id INTEGER,
    stock INTEGER DEFAULT 0,
    activo BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
)
''')

# Alter Table - Agregar columna
imprimir_separador("Alter Table - Agregar columna")
ejecutar_consulta(cursor, '''
ALTER TABLE productos ADD COLUMN IF NOT EXISTS descripcion TEXT
''')

# 2. DML - Comandos de Manipulación de Datos
imprimir_separador("2. DML - Inserción de Datos")

# Insert into categorías
ejecutar_consulta(cursor, '''
INSERT INTO categorias (nombre, descripcion) VALUES
    ('Electrónicos', 'Productos electrónicos y gadgets'),
    ('Hogar', 'Artículos para el hogar'),
    ('Jardín', 'Herramientas y productos de jardinería')
ON CONFLICT (id) DO NOTHING
''')

# Insert into productos
ejecutar_consulta(cursor, '''
INSERT INTO productos (nombre, precio, categoria_id, stock, descripcion) VALUES
    ('Laptop', 999.99, 1, 10, 'Laptop de última generación'),
    ('Smartphone', 499.99, 1, 15, 'Teléfono inteligente'),
    ('Sartén', 29.99, 2, 20, 'Sartén antiadherente'),
    ('Regadera', 15.99, 3, 30, 'Regadera de jardín')
ON CONFLICT (id) DO NOTHING
''')

# Select básico
imprimir_separador("Select básico")
cursor.execute('SELECT * FROM productos')
mostrar_resultados(cursor)

# Select con JOIN
imprimir_separador("Select con JOIN")
cursor.execute('''
SELECT p.nombre, p.precio, c.nombre as categoria
FROM productos p
JOIN categorias c ON p.categoria_id = c.id
''')
mostrar_resultados(cursor)

# Update
imprimir_separador("Update")
ejecutar_consulta(cursor, '''
UPDATE productos
SET precio = 449.99
WHERE nombre = 'Smartphone'
''')

# Select con WHERE
imprimir_separador("Select con WHERE")
cursor.execute('SELECT nombre, precio FROM productos WHERE precio < 500')
mostrar_resultados(cursor)

# Delete
imprimir_separador("Delete")
ejecutar_consulta(cursor, '''
DELETE FROM productos
WHERE nombre = 'Sartén'
''')

# 3. Consultas Avanzadas
imprimir_separador("3. Consultas Avanzadas")

# Group By y funciones agregadas
cursor.execute('''
SELECT c.nombre as categoria,
        COUNT(*) as total_productos,
        AVG(precio) as precio_promedio,
        MAX(precio) as precio_maximo
FROM productos p
JOIN categorias c ON p.categoria_id = c.id
GROUP BY c.nombre
''')
mostrar_resultados(cursor)

# Crear Vista
imprimir_separador("Crear Vista")
ejecutar_consulta(cursor, '''
CREATE OR REPLACE VIEW productos_por_categoria AS
SELECT c.nombre as categoria,
        COUNT(*) as total_productos,
        SUM(stock) as stock_total
FROM productos p
JOIN categorias c ON p.categoria_id = c.id
GROUP BY c.nombre
''')

# Consultar Vista
cursor.execute('SELECT * FROM productos_por_categoria')
mostrar_resultados(cursor)

# Crear Índice
imprimir_separador("Crear Índice")
ejecutar_consulta(cursor, '''
CREATE INDEX IF NOT EXISTS idx_productos_nombre
ON productos(nombre)
''')

# Ejemplo de CASE
imprimir_separador("Ejemplo de CASE")
cursor.execute('''
SELECT nombre,
        CASE
            WHEN precio < 100 THEN 'Económico'
            WHEN precio < 500 THEN 'Intermedio'
            ELSE 'Premium'
        END as categoria_precio
FROM productos
''')
mostrar_resultados(cursor)

# Commit y cerrar conexión
conexion.commit()
conexion.close()
print("\nDemostración completada. Conexión cerrada.")