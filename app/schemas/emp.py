from pydantic import BaseModel
from typing import Optional
from datetime import date


class EMPResponse(BaseModel):
    empno: int
    ename: str
    job: str
    mgr: int | None
    hiredate: date
    sal: int
    comm: int | None
    deptno: int

    class Config:
        from_attributes = True


class EMPCreate(BaseModel):
    ename: str
    sal: int
    comm: Optional[int]


class NameResponse(BaseModel):
    name: str


class EmployeeInfo(BaseModel):
    name: str
    department_no: int
    salary: int
