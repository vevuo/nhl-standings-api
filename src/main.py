import os

from fastapi import FastAPI
from mangum import Mangum

stage = os.environ.get('STAGE', None)
openapi_prefix = f"/{stage}" if stage else "/"

app = FastAPI(title="NHL Standings API", openapi_prefix=openapi_prefix)


# @app.get("/")
# async def index():
#    return {"message": "NHL standings API. See /docs or /redoc"}


@app.get("/standings/division")
async def list_current_standings_by_division():
    return {"division": "division"}


@app.get("/standings/conference")
async def list_current_standings_by_conference():
    return {"conference": "conference"}


@app.get("/standings/league")
async def list_current_league_standings():
    return {"league": "league"}


@app.get("/standings/{year}/{type}")
async def list_standings_by_year(year: int, type: str):
    return {"year": year, "type": type}


@app.get("/teams")
async def list_all_teams():
    return [
        {"team_name": "Montreal Canadiens"}
    ]


@app.get("/team/{team_id}")
async def list_team_details_by_id(team_id: int):
    return {"team_id": team_id}


handler = Mangum(app)
