from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_current_standings():
    return {"division": "division"}


@router.get("/division")
async def list_current_division_standings():
    return {"division": "division"}


@router.get("/conference")
async def list_current_conference_standings():
    return {"conference": "conference"}


@router.get("/league")
async def list_current_league_standings():
    return {"league": "league"}


@router.get("/{year}/{type}")
async def list_standings_by_year(year: int, type: str):
    return {"year": year, "type": type}
