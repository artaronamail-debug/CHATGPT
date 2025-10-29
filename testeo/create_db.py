import sqlite3
import os

DB_PATH = "propiedades.db"

# Eliminar DB existente para empezar fresco
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Crear tabla
cur.execute('''
CREATE TABLE properties (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    neighborhood TEXT,
    price INTEGER,
    rooms INTEGER,
    sqm INTEGER,
    description TEXT,
    operacion TEXT
)
''')

# Insertar datos de ejemplo
properties = [
    ("Departamento en Palermo Soho", "Palermo", 45000, 2, 65, "Hermoso depto en Palermo Soho con balcón", "alquiler"),
    ("Casa en Recoleta", "Recoleta", 850000, 3, 120, "Casa moderna en Recoleta con jardín", "venta"),
    ("PH en Belgrano", "Belgrano", 38000, 1, 45, "PH acogedor en Belgrano R", "alquiler"),
    ("Departamento en Palermo Hollywood", "Palermo", 52000, 3, 80, "Depto luminoso en Palermo Hollywood", "alquiler"),
    ("Casa en Caballito", "Caballito", 720000, 4, 150, "Casa familiar en Caballito", "venta"),
    ("Monoambiente en Palermo", "Palermo", 35000, 1, 35, "Monoambiente funcional en Palermo", "alquiler"),
    ("Departamento en Recoleta", "Recoleta", 48000, 2, 70, "Depto con vista en Recoleta", "alquiler")
]

cur.executemany('''
INSERT INTO properties (title, neighborhood, price, rooms, sqm, description, operacion)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', properties)

conn.commit()
conn.close()
print("✅ Base de datos creada con 7 propiedades de ejemplo")