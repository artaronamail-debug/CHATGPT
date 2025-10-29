# test_models.py - Prueba solo modelos confirmados
import requests

def test_confirmed_models():
    api_key = "AIzaSyALNEvJuxr5FYX6q04XAF6ppzkf4avnOig"
    prompt = "Responde solo con OK"
    
    # Modelos MÁS probables que funcionen (de tu lista)
    models_to_test = [
        "gemini-2.0-flash-001",      # Modelo estable
        "gemini-2.0-flash",          # Alternativa flash
        "gemini-pro-latest",         # Pro más reciente
        "gemini-2.5-flash",          # Si está habilitado
        "gemini-pro",                # Pro básico
    ]
    
    base_url = "https://generativelanguage.googleapis.com/v1beta/models"
    
    for model in models_to_test:
        url = f"{base_url}/{model}:generateContent?key={api_key}"
        print(f"\n🧪 Probando: {model}")
        
        try:
            response = requests.post(
                url,
                headers={"Content-Type": "application/json"},
                json={"contents": [{"parts": [{"text": prompt}]}]},
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                text = data["candidates"][0]["content"]["parts"][0]["text"]
                print(f"✅ ✅ ✅ FUNCIONA: {model} -> {text}")
                return model  # Devolver el primer modelo que funcione
            else:
                print(f"❌ {model}: Error {response.status_code}")
                if response.status_code == 404:
                    print(f"   Mensaje: {response.json().get('error', {}).get('message', '')}")
                
        except Exception as e:
            print(f"💥 {model}: Excepción - {e}")
    
    return None

if __name__ == "__main__":
    working_model = test_confirmed_models()
    if working_model:
        print(f"\n🎯 MODELO QUE FUNCIONA: {working_model}")
        print(f"🔧 Usa este modelo en tu config.py")
    else:
        print("\n😞 Ningún modelo funcionó")
        print("💡 Usaremos el sistema de respuestas predefinidas")