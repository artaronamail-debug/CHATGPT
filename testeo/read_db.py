import sqlite3
import pandas as pd
import os

# Ruta a la base de datos
DB_PATH = os.path.join(os.path.dirname(__file__), "conversaciones.db")

# Comprobar si la base de datos existe
if not os.path.exists(DB_PATH):
    print(f"No se pudo encontrar el archivo de la base de datos en la ruta: {DB_PATH}")
else:
    try:
        # Conexión a la base de datos
        conn = sqlite3.connect(DB_PATH)

        # Leer datos de la tabla 'logs'
        df = pd.read_sql_query("SELECT * FROM logs", conn)

        # Cerrar la conexión
        conn.close()

        # Imprimir el DataFrame
        if not df.empty:
            print(df.to_string())
        else:
            print("La tabla 'logs' está vacía o no existe.")

    except sqlite3.OperationalError as e:
        print(f"Error al leer la base de datos: {e}")
        print("Es posible que la tabla 'logs' no exista.")