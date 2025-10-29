import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "propiedades.db")

def verificar_estructura():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    # Verificar las columnas de la tabla properties
    cur.execute("PRAGMA table_info(properties)")
    columnas = cur.fetchall()
    
    print("🔍 ESTRUCTURA DE LA TABLA 'properties':")
    print("Columnas disponibles:")
    for col in columnas:
        print(f"  - {col[1]} ({col[2]})")
    
    # Verificar si existe datos
    cur.execute("SELECT COUNT(*) FROM properties")
    count = cur.fetchone()[0]
    print(f"📊 Total de propiedades en la BD: {count}")
    
    conn.close()

if __name__ == "__main__":
    verificar_estructura()