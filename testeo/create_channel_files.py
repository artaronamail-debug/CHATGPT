import json
import os
import shutil

def create_channel_files():
    """Crea archivos JSON para cada canal basados en properties.json"""
    
    # Cargar el properties.json principal
    try:
        with open("properties.json", "r", encoding="utf-8") as f:
            propiedades = json.load(f)
    except Exception as e:
        print(f"❌ Error cargando properties.json: {e}")
        return False
    
    # Crear carpeta data si no existe
    os.makedirs("data", exist_ok=True)
    
    # Canales que necesitas
    canales = ["web", "whatsapp", "telegram", "facebook"]
    
    for canal in canales:
        archivo_destino = f"data/{canal}.json"
        
        # Copiar las mismas propiedades para todos los canales
        with open(archivo_destino, "w", encoding="utf-8") as f:
            json.dump(propiedades, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Creado: {archivo_destino}")
    
    print("🎉 Archivos por canal creados exitosamente!")
    return True

if __name__ == "__main__":
    create_channel_files()