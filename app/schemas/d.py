from pydantic import BaseModel
from typing import Optional


class DCreate(BaseModel):
    id: Optional[int]
