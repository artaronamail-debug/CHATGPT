# test_final_completo.py
import requests
import datetime

def test_completo():
    print("🎯 TEST FINAL - SISTEMA COMPLETO")
    print("=" * 50)
    print(f"⏰ {datetime.datetime.now()}")
    
    # 1. Test Render
    print("1. 🔍 Probando Render...")
    try:
        response = requests.get("https://chatgpt-eio1.onrender.com", timeout=10)
        print(f"   ✅ Render: Status {response.status_code}")
    except Exception as e:
        print(f"   ❌ Render: {e}")
        return False
    
    # 2. Test Chatbot
    print("2. 💬 Probando Chatbot...")
    try:
        response = requests.post(
            "https://chatgpt-eio1.onrender.com/chat",
            json={"message": "Hola, ¿está todo funcionando?", "channel": "web"},
            timeout=30
        )
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Chatbot: {data.get('respuesta_bot', 'Sin respuesta')}")
        else:
            print(f"   ❌ Chatbot: Status {response.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ Chatbot: {e}")
        return False
    
    print("3. 🌐 ¡SISTEMA 100% OPERATIVO! 🎉")
    print("   📱 URL pública: https://dantearona-collab.github.io/CHATGPT/")
    return True

if __name__ == "__main__":
    test_completo()