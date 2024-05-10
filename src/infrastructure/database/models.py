from typing import Optional
from uuid import UUID

from sqlalchemy import BigInteger, String, Uuid
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
    pass


class UserModel(Base):
    __tablename__ = 'users'
    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    language: Mapped[Optional[str]] = mapped_column(String(2), nullable=True)
