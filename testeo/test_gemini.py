from config import API_KEYS
from gemini.client import call_gemini_with_rotation

if __name__ == "__main__":
    print("🧪 Iniciando prueba de rotación de claves con Gemini...\n")

    if not API_KEYS:
        print("❌ No se encontraron claves en el entorno. Verificá el archivo .env.")
    else:
        for i, key in enumerate(API_KEYS):
            respuesta = call_gemini_with_rotation("Respondé solo con OK")
            print(f"🔑 Clave {i+1} ({key[:10]}...): {respuesta}")




# from gemini.client import call_gemini_with_rotation

# if __name__ == "__main__":
#     prompt = "Respondé solo con OK"
#     print("🧪 Iniciando prueba de rotación de claves con Gemini...\n")
#     respuesta = call_gemini_with_rotation(prompt)
#     print(f"\n✅ Resultado final: {respuesta}")


# for i, key in enumerate(API_KEYS):
#     print(f"\n🔑 Probando clave {i+1} ({key[:10]}...):")
#     respuesta = call_gemini_with_rotation("Respondé solo con OK")
#     print(f"✅ Respuesta: {respuesta}")
    
    
# from gemini.client import call_gemini

# respuesta = call_gemini("Respondé solo con OK", "AIzaSyBhHLAKgce6X7QpjJJrEkmvh_8U1RyNd0A")
# print(respuesta)

# from gemini.client import call_gemini_with_rotation

# print(call_gemini_with_rotation("¿Qué propiedades hay en Caballito?"))