from fastapi import APIRouter

router = APIRouter()


@router.get("/teams")
async def list_all_teams():
    return [
        {"team_name": "Montreal Canadiens"}
    ]


@router.get("/team/{team_id}")
async def list_team_details_by_id(team_id: int):
    return {"team_id": team_id}
