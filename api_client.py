import httpx

async def call_external_api(url: str):
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        return resp.json()
