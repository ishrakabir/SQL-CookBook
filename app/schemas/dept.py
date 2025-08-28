from pydantic import BaseModel
from typing import Optional


class DEPTBase(BaseModel):
    dname: str
    loc: str


class DEPTCreate(DEPTBase):
    deptno: int


class DEPTResponse(DEPTBase):
    deptno: int
    dname: str
    loc: str

    class Config:
        orm_mode = True


class DEPTEMPResponse(BaseModel):
    deptno: Optional[int]  
    dname: Optional[str]
    ename: Optional[str]
