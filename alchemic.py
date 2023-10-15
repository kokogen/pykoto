import asyncio
from enum import Enum
from typing import List
from typing import Generator
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.dialects.postgresql import ARRAY

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker


engine = create_async_engine(
    'postgresql+asyncpg://postgres:postgres@localhost:5432/postgres',
    future=True,
    echo=True,
    execution_options={"isolation_level": "AUTOCOMMIT"},
)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def get_db() -> Generator:
    """Dependency for getting async session"""
    try:
        session: AsyncSession = async_session()
        yield session
    finally:
        await session.close()

class NodeType(str, Enum):
    DAG_OP = 'DAG_OPERATION'
    DAG_EDV = 'ENTITY_DATAVERSION'
    
class Base(DeclarativeBase):
    pass

class Dag(Base):
    __tablename__ = 'dag'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    params: Mapped[List[str]] = mapped_column(ARRAY(String), nullable=False)

class Node(Base):
    __tablename__ = 'node'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    node_type: Mapped['NodeType'] = mapped_column(String(10), nullable=False)   

if __name__ == '__main__':
    print('Lets go!')
    Base.metadata.create_all(engine)