from fastapi import FastAPI

app = FastAPI(title="Chipahua", version="0.1.0")

@app.get("/")
def root():
    return {"name": "Chipahua", "status": "ok"}