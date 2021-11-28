"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
import os
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Text,
)
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, declared_attr

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://user:password@localhost/postgres"

engine = create_async_engine(
    PG_CONN_URI,
    echo=True,
)

Session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


class Base:
    """
    Базовая модель для создания таблиц
    """
    @declared_attr
    def __tablename__(cls):
        return f"blog_app__{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)


class User(Base):
    """
    Модель таблицы пользователя
    """
    name = Column(String(32), unique=True)
    username = Column(String(32), unique=True)
    email = Column(String(32), unique=True)

    posts = relationship("Post", back_populates="user")


class Post(Base):
    """
    Модель таблицы постов
    """
    title = Column(String(256), nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")
    user_id = Column(Integer, ForeignKey("blog_app__users.id"), nullable=True)

    user = relationship("User", back_populates="posts")