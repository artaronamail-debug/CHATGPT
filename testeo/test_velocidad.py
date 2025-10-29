# test_velocidad.py
import requests
import time

def test_velocidad():
    print("⏱️ TEST DE VELOCIDAD")
    print("=" * 50)
    
    mensajes = ["Hola", "OK", "Test"]
    
    for msg in mensajes:
        inicio = time.time()
        
        try:
            response = requests.post(
                "http://127.0.0.1:8000/chat",
                json={"message": msg, "channel": "web"},
                timeout=60
            )
            
            duracion = time.time() - inicio
            
            if response.status_code == 200:
                print(f"✅ '{msg}': {duracion:.2f}s")
            else:
                print(f"❌ '{msg}': {duracion:.2f}s - Error {response.status_code}")
                
        except Exception as e:
            print(f"💥 '{msg}': Error - {e}")

if __name__ == "__main__":
    test_velocidad()