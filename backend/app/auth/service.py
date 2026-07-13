from sqlalchemy.orm import Session

from app.auth.hashing import hash_password, verify_password
from app.auth.jwt import create_access_token
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.auth import UserRegister


class AuthService:

    def __init__(self):
        self.user_repository = UserRepository()

    def register(
        self,
        db: Session,
        user: UserRegister,
    ) -> User:

        existing_user = self.user_repository.get_by_email(
            db,
            user.email,
        )

        if existing_user:
            raise ValueError("Email already registered")

        new_user = User(
            username=user.username,
            email=user.email,
            hashed_password=hash_password(user.password),
        )

        return self.user_repository.create(
            db,
            new_user,
        )

    def login(
        self,
        db: Session,
        username: str,
        password: str,
    ):

        user = self.user_repository.get_by_email(
            db,
            username,
        )

        if user is None:
            raise ValueError("Invalid email or password")

        if not verify_password(
            password,
            user.hashed_password,
        ):
            raise ValueError("Invalid email or password")

        access_token = create_access_token(
            {
                "sub": str(user.id)
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer",
        }