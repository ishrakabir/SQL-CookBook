from pydantic import BaseModel
from typing import List


class InsertDeptEastRequest(BaseModel):
    locations: List[str]
