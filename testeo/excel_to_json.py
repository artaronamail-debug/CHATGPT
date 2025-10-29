import pandas as pd
import json

# Cargar Excel
df = pd.read_excel("propiedades.xlsx")

# Convertir a lista de dicts
data = df.to_dict(orient="records")

# Guardar como JSON
with open("properties.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Archivo properties.json actualizado.")
def create_channel_files():
    """Crear archivos por canal después de generar properties.json"""
    import os
    import shutil
    
    # Crear carpeta data si no existe
    os.makedirs("data", exist_ok=True)
    
    canales = ["web", "whatsapp", "telegram"]
    
    for canal in canales:
        archivo_destino = f"data/{canal}.json"
        shutil.copy2("properties.json", archivo_destino)
        print(f"✅ Creado: {archivo_destino}")

# Llamar esta función después de generar properties.json
create_channel_files()
