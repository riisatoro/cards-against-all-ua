from fastapi import APIRouter

from api.auth.schemas import CommonResponseSchema


router = APIRouter(
    tags=['Health check']
)

@router.get('/health', response_model=CommonResponseSchema)
def health_check() -> CommonResponseSchema:
    return CommonResponseSchema(detail='ok')
