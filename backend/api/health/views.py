from fastapi import APIRouter

from api.auth.schemas import CommonResponse


router = APIRouter(
    tags=['Health check']
)

@router.get('/health')
def health_check() -> CommonResponse:
    return CommonResponse
