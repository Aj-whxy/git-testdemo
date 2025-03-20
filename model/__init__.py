from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 这是我添加的注释语句

engine = create_async_engine("sqlite+aiosqlite:///test.db", echo=True)

AsyncSessionFactory = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False,autoflush=True)

Base = declarative_base()

from . import user
