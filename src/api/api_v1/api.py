from fastapi import APIRouter

from .endpoints import teams
from .endpoints import standings

router = APIRouter()
router.include_router(teams.router, prefix="/teams", tags=["Teams"])
router.include_router(standings.router, prefix="/standings", tags=["Standings"])
