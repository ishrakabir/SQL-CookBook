from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.database import Base


class V(Base):
    __tablename__ = "v"
    data = Column(String, primary_key=True)


class V2(Base):
    __tablename__ = "v2"
    job = Column(String, primary_key=True)
    ename = Column(String, primary_key=True)
    sal = Column(Integer, primary_key=True)


class V3(Base):
    __tablename__ = "v3"
    empno = Column(Integer, primary_key=True, index=True)
    ename = Column(String(10), nullable=False)
    job = Column(String(9))
    mgr = Column(Integer, ForeignKey("emp.empno"))
    hiredate = Column(Date)
    sal = Column(Integer)
    comm = Column(Integer)
    deptno = Column(Integer, ForeignKey("dept.deptno"))
