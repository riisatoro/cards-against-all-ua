from fastapi import APIRouter, HTTPException, status

from api.auth.schemas import CommonResponse, NewUser


router = APIRouter(
    prefix='/auth',
    tags=['Authentication and authorization'],
)

@router.post('/register', response_model=CommonResponse)
def register(new_user: NewUser):
    if NewUser.password != NewUser.repeat_password:
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
