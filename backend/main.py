
import uvicorn
from fastapi import FastAPI

from api.auth.views import router as auth_router
from api.game.views import router as game_router
from api.health.views import router as health_router


app = FastAPI()

app.include_router(auth_router)
app.include_router(game_router)
app.include_router(health_router)
