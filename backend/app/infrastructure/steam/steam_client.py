import httpx
from app.config import settings

BASE_URL = "https://api.steampowered.com"

class SteamClient:
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or settings.steam_api_key

    async def get_own_games(self, steam_id: str) -> list[dict]:
        """
        Trae los juegos de un usuario con su tiempo de juego.
        
        Parametros:
        steam_id (str): El ID de Steam del usuario.

        Retorna:
        list[dict]: Una lista de diccionarios que representan los juegos del usuario.
        """
        url = f"{BASE_URL}/IPlayerService/GetOwnedGames/v1/"
        params = {
            "key": self.api_key,
            "steamid": steam_id,
            "include_appinfo": True,
            "include_played_free_games": True,
            "format": "json"
        }

        async with httpx.AsyncClient(timeout=20) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()
        return data.get("response", {}).get("games", [])
