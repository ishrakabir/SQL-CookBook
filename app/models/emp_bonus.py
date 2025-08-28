from sqlalchemy import Column, Integer, Date
from app.database import Base


class EmpBonus(Base):
    __tablename__ = "emp_bonus"

    empno = Column(Integer, primary_key=True, index=True)
    received = Column(Date, nullable=False)
    type = Column(Integer, nullable=False)
