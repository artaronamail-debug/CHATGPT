from fastapi import FastAPI
import google.generativeai as genai
import os

app = FastAPI()

# Configurar Gemini con variable de entorno
API_KEY = os.getenv('GEMINI_API_KEY')
if API_KEY:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-2.5-flash')

@app.get("/")
async def root():
    return {"message": "✅ Gemini API está funcionando"}

@app.get("/chat")
async def chat(prompt: str = "Hola"):
    try:
        if not API_KEY:
            return {"error": "API Key no configurada"}
        
        response = model.generate_content(prompt)
        return {"respuesta": response.text}
    except Exception as e:
        return {"error": str(e)}

# Health check esencial para Render
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)