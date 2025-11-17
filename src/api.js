export async function diagnosticoGemini(clave) {
  try {
    const res = await fetch(`https://dante-chatbot-api-production.up.railway.app/diagnostico?clave=${clave}`);
    const data = await res.json();
    return data;
  } catch (error) {
    console.error("❌ Error al conectar con el backend:", error);
    return { valida: false, error: "No se pudo conectar con el servidor" };
  }
}