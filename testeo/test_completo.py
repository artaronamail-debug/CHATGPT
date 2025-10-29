# test_completo.py - Verificar toda la configuración
from config import API_KEYS, WORKING_MODEL, ENDPOINT
from gemini.client import call_gemini_with_rotation

print("🧪 TEST COMPLETO DEL SISTEMA")
print("=" * 50)

print(f"🔧 Modelo: {WORKING_MODEL}")
print(f"🔑 Claves: {[k[:10] for k in API_KEYS]}")
print(f"🌐 Endpoint: {ENDPOINT}")

# Test simple
response = call_gemini_with_rotation("Responde solo con OK")
print(f"\n🎯 RESULTADO: {response}")

if "OK" in response:
    print("✅ ✅ ✅ SISTEMA FUNCIONANDO CORRECTAMENTE")
else:
    print("❌ ❌ ❌ HAY PROBLEMAS EN LA CONFIGURACIÓN")