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

    def create(
        self,
        db: Session,
        user: User,
    ) -> User:

        db.add(user)

        db.commit()

        db.refresh(user)

        return user