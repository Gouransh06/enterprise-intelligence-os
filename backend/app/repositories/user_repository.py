from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:

    def get_by_email(
        self,
        db: Session,
        email: str,
    ) -> User | None:

        stmt = select(User).where(User.email == email)

        return db.scalar(stmt)

    def get_by_username(
        self,
        db: Session,
        username: str,
    ) -> User | None:

        stmt = select(User).where(User.username == username)

        return db.scalar(stmt)

    def get_by_id(
        self,
        db: Session,
        user_id: int,
    ) -> User | None:

        stmt = select(User).where(User.id == user_id)

        return db.scalar(stmt)

    def create(
        self,
        db: Session,
        user: User,
    ) -> User:

        db.add(user)
        db.commit()
        db.refresh(user)

        return user