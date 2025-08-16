from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.database import Base


class EMP(Base):
    __tablename__ = "emp"

    empno = Column(Integer, primary_key=True, index=True)
    ename = Column(String(10), nullable=False)
    job = Column(String(9))
    mgr = Column(Integer, ForeignKey("emp.empno"))
    hiredate = Column(Date)
    sal = Column(Integer)
    comm = Column(Integer)
    deptno = Column(Integer, ForeignKey("dept.deptno"))
