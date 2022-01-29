from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

meta = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }
)

Base = declarative_base(metadata=meta)


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)


class Entry(BaseModel):
    __tablename__ = "Entries"

    amount_in_cents = Column(Integer, nullable=False, default=0)
    user_id = Column(Integer, ForeignKey('Users.id'), nullable=False)
    user = relationship(
        "User",
        back_populates="entries",
    )


class User(BaseModel):
    __tablename__ = "Users"

    user_name = Column(String(80), unique=True, nullable=False)
    entries = relationship(
        "Entry",
        back_populates="user",
        cascade="all, delete-orphan",
    )
