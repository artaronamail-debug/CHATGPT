# test_nueva_clave.py - Probar la nueva clave
import requests
import os
from dotenv import load_dotenv
from pathlib import Path

# Cargar .env
dotenv_path = Path("C:/Users/artar/downloads/chatgpt/.env")
load_dotenv(dotenv_path)

# Obtener la nueva clave
nueva_key = os.getenv("GEMINI_KEYS", "").strip()
print(f"🔑 Nueva clave: {nueva_key[:10]}...")

if not nueva_key:
    print("❌ No se encontró la clave en .env")
    exit()

# Probar la nueva clave
model = "gemini-2.0-flash-001"
url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={nueva_key}"

try:
    response = requests.post(
        url,
        headers={"Content-Type": "application/json"},
        json={"contents": [{"parts": [{"text": "Responde solo con OK"}]}]},
        timeout=10
    )
    
    print(f"📥 Status: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        text = data["candidates"][0]["content"]["parts"][0]["text"]
        print(f"✅ ✅ ✅ NUEVA CLAVE FUNCIONA: {text}")
    else:
        print(f"❌ Error: {response.text}")
        
except Exception as e:
    print(f"💥 Excepción: {e}")