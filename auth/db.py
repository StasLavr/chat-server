import os 
import sys
import datetime
from typing import AsyncGenerator
from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase 
from sqlalchemy import Column, Integer, String, TIMESTAMP
current_dir = os.path.dirname(os.path.abspath(__file__))
subfolder_path = os.path.join(current_dir, '..')
sys.path.append(subfolder_path)
from conf import db_url 

DATABASE_URL = db_url
class Base(DeclarativeBase):
    pass

class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    fullname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    
engine = create_async_engine(db_url)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
