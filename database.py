from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from dbconfig import DB_URL
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer

class Base(DeclarativeBase):
    pass

metadata = Base.metadata

async_egine = create_async_engine(DB_URL)

async_session = async_sessionmaker(async_egine, expire_on_commit=False)

class Task(Base):
    __tablename__ = "task"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
