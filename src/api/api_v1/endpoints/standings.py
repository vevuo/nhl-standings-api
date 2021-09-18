from fastapi import APIRouter

router = APIRouter()


@router.get("/standings/division")
async def list_current_standings_by_division():
    return {"division": "division"}


@router.get("/standings/conference")
async def list_current_standings_by_conference():
    return {"conference": "conference"}


@router.get("/standings/league")
async def list_current_league_standings():
    return {"league": "league"}


@router.get("/standings/{year}/{type}")
async def list_standings_by_year(year: int, type: str):
    return {"year": year, "type": type}
