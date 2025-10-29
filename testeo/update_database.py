import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "propiedades.db")

def agregar_columna_operacion():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    try:
        # Agregar la columna operacion si no existe
        cur.execute("ALTER TABLE properties ADD COLUMN operacion TEXT")
        print("✅ Columna 'operacion' agregada a la tabla properties")
        
        # Si quieres, también puedes agregar datos de ejemplo
        # o actualizar los registros existentes con valores por defecto
        cur.execute("UPDATE properties SET operacion = 'venta' WHERE operacion IS NULL")
        print("✅ Valores por defecto asignados")
        
        conn.commit()
        
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            print("ℹ️ La columna 'operacion' ya existe")
        else:
            print(f"❌ Error: {e}")
    
    conn.close()

if __name__ == "__main__":
    agregar_columna_operacion()