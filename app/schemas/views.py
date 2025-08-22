from pydantic import BaseModel


class VResponse(BaseModel):
    data: str

    class Config:
        orm_mode = True
