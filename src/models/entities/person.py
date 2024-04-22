from src.models.settings.base import Base
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.sql import func

class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    document = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    phone = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())