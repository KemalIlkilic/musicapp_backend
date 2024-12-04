from fastapi import APIRouter, HTTPException , status , Depends, BackgroundTasks
from fastapi.responses import JSONResponse
from .schemas import UserCreateModel, UserLoginModel
from .service import UserService
from typing import Annotated
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from .utils import verify_password



user_service = UserService()
auth_router = APIRouter()
MyAsyncSession = Annotated[AsyncSession, Depends(get_session)]


@auth_router.get('/')
async def test():
    return {'message' : 'Hello World'}


@auth_router.post('/signup', status_code=status.HTTP_201_CREATED)
async def create_user_account(user_data : UserCreateModel, session : MyAsyncSession ):
    email = user_data.email
    is_exist = await user_service.user_exists_by_email(email , session)
    if is_exist:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="A user with this email already exists."
        )
    new_user = await user_service.create_user(user_data, session)
    return { "user": new_user }

@auth_router.post('/login')
async def login_users(login_data: UserLoginModel, session : MyAsyncSession):
    email = login_data.email
    password = login_data.password
    is_exist = await user_service.user_exists_by_email(email, session)
    if is_exist:
        user = await user_service.get_user_by_email(email,session)
        hashed_password_in_database = user.password_hash
        is_password_true = verify_password(password, hashed_password_in_database )
        if is_password_true:
            return JSONResponse(
                content={
                    "message":"Login succesfull",
                    "user": {
                        "email":user.email,
                        "uid":str(user.uid)
                    }
                }
            )
    raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid Email Or Password"
        )