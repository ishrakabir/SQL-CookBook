from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.emp import (
    EMPResponse,
    NameResponse,
    EmployeeInfo,
    SalaryCommissionResponse,
    EmployeeMessageResponse,
    EmployeStatusResponse,
)
from app.services.retrieving_records import (
    get_low_salary_employees,
    finding_rows_that_satisfy_multiple_conditions,
    retrieving_a_subset_of_column,
    providing_meaningful_names,
    referencing_an_aliased_column_in_the_where_clause,
    concatenating_column,
    using_conditional_logic,
    limiting_the_number,
    returning_n_random_records,
    transforming_null_into_real,
    finding_null,
    searching_for_patterns,
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


@router.get(
    "/referencing-an-aliased-column-in-the-where-clause",
    response_model=list[SalaryCommissionResponse],
)
async def referencing_an_aliased_column_in_the_where_clause_available(
    db: AsyncSession = Depends(get_db),
):
    return await referencing_an_aliased_column_in_the_where_clause(db)


@router.get(
    "/concatenating-column",
    response_model=list[EmployeeMessageResponse],
)
async def concatenating_column_values(
    dept_no: int = Query(...),
    db: AsyncSession = Depends(get_db),
):
    return await concatenating_column(db, dept_no)


@router.get(
    "/using-condtional-logic",
    response_model=list[EmployeStatusResponse],
)
async def using_conditional_logic_in_a_select_statement(
    db: AsyncSession = Depends(get_db),
):
    return await using_conditional_logic(db)


@router.get(
    "/limiting-the-number",
    response_model=list[EMPResponse],
)
async def limiting_the_number_of_rows_returned(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(5, ge=1, le=100, description="Maximum number of records to return"),
    db: AsyncSession = Depends(get_db),
):
    return await limiting_the_number(db, skip, limit)


@router.get(
    "/returning-n-random-records",
    response_model=list[EMPResponse],
)
async def returning_n_random_records_from_a_table(
    limit: int = Query(5, ge=1, le=100, description="Maximum number of records to return"),
    db: AsyncSession = Depends(get_db),
):
    return await returning_n_random_records(db, limit)


@router.get(
    "/finding-null",
    response_model=list[EMPResponse],
)
async def finding_null_values(
    limit: int = Query(5, ge=1, le=100, description="Maximum number of records to return"),
    db: AsyncSession = Depends(get_db),
):
    return await finding_null(db, limit)


@router.get(
    "/transforming-null-into-real",
    response_model=list[dict],
)
async def transforming_null_into_real_values(
    limit: int = Query(5, ge=1, le=100, description="Maximum number of records to return"),
    db: AsyncSession = Depends(get_db),
):
    return await transforming_null_into_real(db, limit)


@router.get(
    "/searching-for-patterns",
    response_model=list[dict],
)
async def searching_for_patterns_matching(
    limit: int = Query(5, ge=1, le=100, description="Maximum number of records to return"),
    db: AsyncSession = Depends(get_db),
):
    return await searching_for_patterns(db, limit)
