from fastapi import FastAPI
from app.config import settings

app = FastAPI(title="Play Next", version="1.0.0")

@app.get("/health")
def health_check():
    return {"status": "ok",
            "steam_configuration": bool(settings.steam_api_key and settings.steam_id)   
        }
