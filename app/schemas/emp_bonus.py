from pydantic import BaseModel
from datetime import date
from typing import Optional


class EmpDeptBonusResponse(BaseModel):
    ename: str
    loc: Optional[str]
    received: Optional[date]

    class Config:
        orm_mode = True
class EmpDeptBonusAggregatesResponse(BaseModel):
    deptno: int
    total_sal: int
    total_bonus: int

    class Config:
        orm_mode = True
