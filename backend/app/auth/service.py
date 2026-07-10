from sqlalchemy.orm import Session

from app.auth.hashing import hash_password
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