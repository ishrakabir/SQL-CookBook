from pydantic import BaseModel


class DEPTBase(BaseModel):
    dname: str
    loc: str


class DEPTCreate(DEPTBase):
    deptno: int


class DEPTResponse(DEPTBase):
    deptno: int

    class Config:
        orm_mode = True
