from sqlmodel import Field, Relationship, SQLModel, Column
import sqlalchemy.dialects.postgresql as pg
from datetime import date, datetime
import uuid
from typing import List, Optional

class User(SQLModel, table=True):
    __tablename__ = "users"
    uid : uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    name : str
    email : str
    #The original password is never stored
    password_hash : str = Field(exclude=True)
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    update_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))

    def __repr__(self) -> str:
        return f"< User {self.username} >"
    
#Column is an SQLAlchemy component used to provide detailed information about database columns