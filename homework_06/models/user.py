from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, func, Boolean
from .database import db


class User(db.Model):
    """
    Модель таблицы пользователя
    """
    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True)
    email = Column(String(32), unique=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    is_new = Column(Boolean, nullable=False, default=False, server_default="FALSE")

