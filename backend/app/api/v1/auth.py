from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import traceback

from app.auth.service import AuthService
from app.database.session import get_db
from app.schemas.auth import UserRegister
from app.schemas.user import UserResponse

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"],
)

auth_service = AuthService()


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201,
)
def register(
    user: UserRegister,
    db: Session = Depends(get_db),
):
    try:
        return auth_service.register(db, user)

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )