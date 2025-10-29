
import pandas as pd
import json

# Cargar datos desde el archivo JSON
with open('properties.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Convertir a DataFrame de pandas
df = pd.DataFrame(data)

# Guardar como archivo Excel
df.to_excel('propiedades.xlsx', index=False)

print("El archivo 'propiedades.xlsx' ha sido creado exitosamente.")
