# test_propiedades_final.py
import requests
import time

def test_propiedades_inmobiliarias():
    print("🏠 PRUEBA DE PROPIEDADES - TIMEOUT 30s")
    print("=" * 60)
    
    preguntas_inmobiliarias = [
        "Hola",
        "¿Qué tipos de propiedades tienen disponibles?",
        "¿Cuál es el proceso para alquilar?",
        "¿Requieren garantía propietaria?",
        "¿Aceptan mascotas?"
    ]
    
    for i, pregunta in enumerate(preguntas_inmobiliarias, 1):
        print(f"🏠 Pregunta {i}: {pregunta}")
        inicio = time.time()
        
        try:
            response = requests.post(
                "http://127.0.0.1:8000/chat",
                json={"message": pregunta, "channel": "web"},
                timeout=30  # 30 segundos de timeout
            )
            
            duracion = time.time() - inicio
            
            if response.status_code == 200:
                data = response.json()
                respuesta = data.get("respuesta_bot", "Sin respuesta")
                print(f"✅ [{duracion:.2f}s] Respuesta: {respuesta}")
            else:
                print(f"❌ [{duracion:.2f}s] Error: {response.status_code}")
                
        except requests.exceptions.Timeout:
            duracion = time.time() - inicio
            print(f"⏰ [{duracion:.2f}s] TIMEOUT - Más de 30 segundos")
        except Exception as e:
            duracion = time.time() - inicio
            print(f"💥 [{duracion:.2f}s] ERROR: {e}")
        
        print("-" * 60)
        time.sleep(2)

if __name__ == "__main__":
    test_propiedades_inmobiliarias()