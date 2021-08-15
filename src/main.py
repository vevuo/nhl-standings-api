from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "NHL standings API. See /docs or /redoc"}


@app.get("/teams")
async def list_all_teams():
    return [
        {"team_name": "Montreal Canadiens"}
    ]


@app.get("/team/{team_id}")
async def list_team_details_by_id(team_id: int):
    return {"team_id": team_id}
