from pydantic import BaseModel
from typing import Optional


class VResponse(BaseModel):
    data: str

    class Config:
        orm_mode = True
class V2Response(BaseModel):
    empno: int
    ename: str
    sal: float
    job: Optional[str] = None
    deptno: Optional[int] = None

    class Config:
        from_attributes = True 
