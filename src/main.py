
from fastapi import FastAPI
from mangum import Mangum

from api.api_v1.api import router as api_router


app = FastAPI(title="Kippura NHL Standings API", root_path="/dev")


@app.get("/")
async def root():
    return {"message": "Kippurta NHL standings API. See /docs or /redoc."}


app.include_router(api_router, prefix="api/v1")
handler = Mangum(app)
