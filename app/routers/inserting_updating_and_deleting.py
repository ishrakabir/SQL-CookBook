from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from typing import Optional
from fastapi import Body

from fastapi import APIRouter, Depends
from app.schemas.dept import DEPTCreate
from app.schemas.d import DCreate
from app.schemas.dept_east import InsertDeptEastRequest
from app.services.inserting_updating_and_deleting import (
    inserting_a_new_record,
    inserting_default_values,
    copying_rows_from_one_table_into_another,
)

router = APIRouter()


@router.post("/inserting-a-new-record")
async def inserting_a_new_record_create(dept: DEPTCreate, db: AsyncSession = Depends(get_db)):
    return await inserting_a_new_record(db, dept)


@router.post("/inserting-default-values")
async def inserting_default_values_create(
    dept: Optional[DCreate] = Body(None), db: AsyncSession = Depends(get_db)
):
    return await inserting_default_values(db, dept)


@router.post("/copying_rows_from_one_table_into_another")
async def copying_rows_from_one_table_into_another_create(
    req: InsertDeptEastRequest, db: AsyncSession = Depends(get_db)
):
    return await copying_rows_from_one_table_into_another(db, req.locations)
