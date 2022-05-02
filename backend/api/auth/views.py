from fastapi import APIRouter, HTTPException, status

from api.auth.schemas import CommonResponse


router = APIRouter(
    prefix='/auth',
    tags=['Authentication and authorization']
)

@router.post('/register')
def register(username: str, email: str, password: str, repeat_password: str) -> CommonResponse:
    if password != repeat_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Passwords don\'t match'
        )
    return CommonResponse(detail='Usar have been created successfully')

@router.post('/login')
def login() -> str:
    return 'ok'

@router.post('/refresh')
def refresh() -> str:
    return 'ok'
