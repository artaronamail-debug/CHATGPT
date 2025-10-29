# test_filtro.py
test_messages = [
    "Hola",
    "¿Quién fue Jorge Luis Borges?",
    "¿Qué propiedades tienen?",
    "Explícame qué es el machine learning",
    "Necesito alquilar un departamento"
]

for msg in test_messages:
    print(f"🧪 '{msg}'")
    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json={"message": msg, "channel": "web"},
        timeout=10
    )
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Respuesta: {data.get('respuesta_bot', 'Sin respuesta')}")
    else:
        print(f"❌ Bloqueado: {response.status_code}")
    print("-" * 40)