from sqlalchemy import Column, String
from app.database import Base


class V(Base):
    __tablename__ = "v"
    data = Column(String, primary_key=True)
