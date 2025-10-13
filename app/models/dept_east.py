from sqlalchemy import Column, Integer, String
from app.database import Base


class DeptEast(Base):
    __tablename__ = "dept_east"

    deptno = Column(Integer, primary_key=True)
    dname = Column(String(14))
    loc = Column(String(13))
