from fastapi import FastAPI
from app.config import settings
from app.infrastructure.steam.steam_client import SteamClient

app = FastAPI(title="Play Next", version="1.0.0")

@app.get("/health")
def health_check():
    return {"status": "ok",
            "steam_configuration": bool(settings.steam_api_key)   
        }   

@app.get("/steam/library")
async def library():
    client = SteamClient()
    games = await client.get_own_games(settings.steam_id)
    return {"total": len(games), 
            "games": games[:10]
        } # Return only the first 10 games for brevity
