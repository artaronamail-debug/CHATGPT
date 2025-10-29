# keep_alive_local.py
import requests
import time
import datetime

def ping_render():
    # ⚠️ REEMPLAZA CON TU URL REAL DE RENDER
    RENDER_URL = "https://tu-app.onrender.com"
    
    print(f"🔄 Iniciando keep-alive para: {RENDER_URL}")
    print("💡 Este script debe mantenerse ejecutándose en tu computadora")
    
    while True:
        try:
            response = requests.get(RENDER_URL, timeout=10)
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"✅ [{timestamp}] Ping exitoso - Status: {response.status_code}")
        except Exception as e:
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"❌ [{timestamp}] Error: {e}")
        
        # Esperar 10 minutos (600 segundos)
        print("⏰ Esperando 10 minutos...")
        time.sleep(600)

if __name__ == "__main__":
    ping_render()