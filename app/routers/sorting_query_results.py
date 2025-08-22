from typing import Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.emp import EmployeeSortedSalary, EmployeeSortedJob, EMPCreate, EMPResponse
from app.schemas.views import VResponse


from app.services.sorting_query_results import (
    returning_query_results,
    sorting_by_multiple_fields,
    sorting_by_substrings,
    sorting_mixed_alphanumeric,
    dealing_with_nulls_when_sorting,
    sorting_on_a_data_dependent_key,
)

router = APIRouter()


@router.get("/returning-query-results", response_model=list[EmployeeSortedSalary])
async def returning_query_results_in_a_specific_order(
    dept_no: Optional[int] = Query(None), db: AsyncSession = Depends(get_db)
):
    return await returning_query_results(db, dept_no)


@router.get("/sorting-by-multiple-fields", response_model=list[EmployeeSortedSalary])
async def sorting_by_multiple_fields_result(
    dept_no: Optional[int] = Query(None), db: AsyncSession = Depends(get_db)
):
    return await sorting_by_multiple_fields(db, dept_no)


@router.get("/sorting-by-substrings", response_model=list[EmployeeSortedJob])
async def sorting_by_substrings_result(db: AsyncSession = Depends(get_db)):
    return await sorting_by_substrings(db)


@router.get("/sorting-mixed-alphanumeric", response_model=list[VResponse])
async def sorting_mixed_alphanumeric_data(db: AsyncSession = Depends(get_db)):
    return await sorting_mixed_alphanumeric(db)


@router.get("/dealing-with-nulls-when-sorting", response_model=list[EMPCreate])
async def dealing_with_nulls_when_sorting_result(db: AsyncSession = Depends(get_db)):
    return await dealing_with_nulls_when_sorting(db)


@router.get("/sorting-on-a-data-dependent-key", response_model=list[EMPResponse])
async def sorting_on_a_data_dependent_key_results(db: AsyncSession = Depends(get_db)):
    return await sorting_on_a_data_dependent_key(db)
