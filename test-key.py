
        
        
import os
import google.generativeai as genai

keys_raw = os.getenv("GEMINI_API_KEYS")
if not keys_raw:
    raise ValueError("❌ Variable de entorno GEMINI_API_KEYS no está definida.")

API_KEYS = keys_raw.split(",")

for key in API_KEYS:
    try:
        genai.configure(api_key=key)
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content("¿Esta clave funciona?")
        print(f"✅ Clave válida: {key[:8]}... → {response.text[:50]}...")
        break
    except Exception as e:
        print(f"❌ Clave fallida: {key[:8]}... → {type(e).__name__}")