import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "propiedades.db")
JSON_PATH = os.path.join(os.path.dirname(__file__), "properties.json")

def migrar_base_datos():
    """Migrar la base de datos para incluir la columna operacion y actualizar datos"""
    
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    # 1. Agregar columna operacion si no existe
    try:
        cur.execute("ALTER TABLE properties ADD COLUMN operacion TEXT")
        print("✅ Columna 'operacion' agregada")
    except sqlite3.OperationalError:
        print("ℹ️ Columna 'operacion' ya existe")
    
    # 2. Agregar columna tipo si no existe
    try:
        cur.execute("ALTER TABLE properties ADD COLUMN tipo TEXT")
        print("✅ Columna 'tipo' agregada")
    except sqlite3.OperationalError:
        print("ℹ️ Columna 'tipo' ya existe")
    
    # 3. Cargar datos del JSON para actualizar
    try:
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            propiedades_json = json.load(f)
        
        # Actualizar cada propiedad en la BD
        for prop in propiedades_json:
            cur.execute('''
                UPDATE properties 
                SET operacion = ?, tipo = ?
                WHERE title = ? AND neighborhood = ?
            ''', (
                prop.get("Operacion") or prop.get("operacion", ""),
                prop.get("tipo", ""),
                prop.get("title", ""),
                prop.get("neighborhood", "")
            ))
        
        print("✅ Datos de operacion y tipo actualizados desde JSON")
        
    except Exception as e:
        print(f"⚠️ Error actualizando datos: {e}")
    
    conn.commit()
    conn.close()
    print("🎉 Migración completada")

if __name__ == "__main__":
    migrar_base_datos()