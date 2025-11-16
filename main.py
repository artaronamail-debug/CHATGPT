from fastapi import FastAPI
import os
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Backend activo"}

@app.get("/ping")
def ping():
    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)