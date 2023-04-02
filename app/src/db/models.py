import datetime
import uuid
from typing import List
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True,
                unique=True, default=uuid.uuid4)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now())
    items: Mapped[List["Items"]] = relationship()


class Items(Base):
    __tablename__ = 'items'
    id = Column(UUID(as_uuid=True), primary_key=True,
                unique=True, default=uuid.uuid4)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now())
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
