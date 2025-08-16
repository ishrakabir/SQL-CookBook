from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.emp import EMPResponse, NameResponse, EmployeeInfo
from app.services.retrieving_records import (
    get_low_salary_employees,
    finding_rows_that_satisfy_multiple_conditions,
    retrieving_a_subset_of_column,
    providing_meaningful_names,
    referencing_an_aliased_column_in_the_where_clause,
)

router = APIRouter()


@router.get("/low-salary", response_model=list[EMPResponse])
async def low_salary_employees(max_salary: int = Query(...), db: AsyncSession = Depends(get_db)):
    return await get_low_salary_employees(db, max_salary)


@router.get("/finding-rows-that-satisfy-multiple-conditions", response_model=list[EMPResponse])
async def finding_rows_that_satisfy_multiple_conditions_employees(
    dept_no: int = Query(...), db: AsyncSession = Depends(get_db)
):
    return await finding_rows_that_satisfy_multiple_conditions(db, dept_no)


@router.get("/retrieving-a-subset-of-column", response_model=list[NameResponse])
async def retrieving_a_subset_of_column_from_a_table(db: AsyncSession = Depends(get_db)):
    return await retrieving_a_subset_of_column(db)


@router.get("/providing-meaningful-names", response_model=list[EmployeeInfo])
async def providing_meaningful_names_from_table(db: AsyncSession = Depends(get_db)):
    return await providing_meaningful_names(db)


@router.get("/referencing-an-aliased-column-in-the-where-clause", response_model=list[EmployeeInfo])
async def referencing_an_aliased_column_in_the_where_clause_available(
    db: AsyncSession = Depends(get_db),
):
    return await referencing_an_aliased_column_in_the_where_clause(db)
