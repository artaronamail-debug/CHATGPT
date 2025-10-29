import sqlite3
import pandas as pd
import os
from datetime import datetime

# Ruta a la base de datos
DB_PATH = os.path.join(os.path.dirname(__file__), "../conversaciones.db")

# Conexión y creación de tabla si no existe
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        channel TEXT,
        user_message TEXT,
        bot_response TEXT
    )
''')
conn.commit()

# Leer datos si existen
df = pd.read_sql_query("SELECT * FROM logs ORDER BY id DESC", conn)
conn.close()

# Exportar a Excel si hay datos
if not df.empty:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"logs_export_{timestamp}.xlsx"
    df.to_excel(output_path, index=False)
    print(f"✅ Exportación completada: {output_path}")
else:
    print("⚠️ No hay registros en la tabla 'logs'. No se generó archivo.")