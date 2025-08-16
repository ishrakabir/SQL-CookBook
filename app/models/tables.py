from sqlalchemy import Column, Integer
from app.database import Base


class T1(Base):
    __tablename__ = "t1"
    id = Column(Integer, primary_key=True)


class T10(Base):
    __tablename__ = "t10"
    id = Column(Integer, primary_key=True)


class T100(Base):
    __tablename__ = "t100"
    id = Column(Integer, primary_key=True)
