from fastapi import FastAPI
import google.generativeai as genai
import os
import socket
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Configurar Gemini
API_KEY = "AIzaSyAoC9RD4HPE7l5wY8RcnMHS7F1BeXj7ea8" 
if API_KEY:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-2.5-flash')
    print("✅ Gemini configurado correctamente")
else:
    print("❌ API Key no encontrada")

@app.get("/")
async def root():
    return {"message": "✅ Gemini API está funcionando"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/chat")
async def chat(prompt: str = "Hola"):
    try:
        if not API_KEY:
            return {"error": "API Key no configurada"}
        
        response = model.generate_content(prompt)
        return {"respuesta": response.text}
    except Exception as e:
        return {"error": str(e)}

def find_available_port(start_port=8000, end_port=9000):
    """Encuentra un puerto disponible automáticamente"""
    for port in range(start_port, end_port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('0.0.0.0', port))
                return port
        except OSError:
            continue
    return 8000  # Fallback

if __name__ == "__main__":
    import uvicorn
    
    # Encontrar puerto disponible automáticamente
    available_port = find_available_port()
    print(f"🚀 Iniciando servidor en puerto {available_port}")
    
    uvicorn.run(app, host="0.0.0.0", port=available_port)