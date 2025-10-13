from sqlalchemy import Column, Integer
from app.database import Base


class D(Base):
    __tablename__ = "d"

    id = Column(Integer, default=0, primary_key=True)
