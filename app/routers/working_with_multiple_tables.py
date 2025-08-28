from typing import Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db

from app.schemas.emp import EmployeeDeptUnion, EMPViewResponse, EmployeeDeptJoin, EMPCreate
from app.schemas.dept import DEPTResponse, DEPTEMPResponse
from app.schemas.emp_bonus import EmpDeptBonusResponse, EmpDeptBonusAggregatesResponse
from app.services.working_with_multiple_tables import (
    stacking_one_rowset_atop_another,
    combining_related_rows,
    finding_rows_in_common_tables,
    retrieving_rows_from_one_table_that_do_not_correspond,
    adding_joins_to_a_query_without_interfering_with_other_joins,
    determining_whether_two_tables_have_the_same_data,
    identifying_and_avoiding_cartesian_products,
    performing_joins_when_using_aggregates,
    performing_outer_joins_when_using_aggregates,
    returning_missing_data_from_multiple_tables,
    using_nulls_in_operations_and_comparisons,
)

router = APIRouter()


@router.get("/stacking-one-rowset-atop-another", response_model=list[EmployeeDeptUnion])
async def stacking_one_rowset_atop_another_result(
    dept_no: Optional[int] = Query(None), db: AsyncSession = Depends(get_db)
):
    return await stacking_one_rowset_atop_another(db, dept_no)


@router.get("/combining-related-rows", response_model=list[dict])
async def combining_related_rows_results(
    dept_no: int = Query(...), db: AsyncSession = Depends(get_db)
):
    return await combining_related_rows(db, dept_no)


@router.get("/finding-rows-in-common-tables", response_model=list[dict])
async def finding_rows_in_common_tables_between_two_tables(db: AsyncSession = Depends(get_db)):
    return await finding_rows_in_common_tables(db)


@router.get(
    "/retrieving-rows-from-one-table-that-do-not-correspond", response_model=list[DEPTResponse]
)
async def retrieving_rows_from_one_table_that_do_not_correspond_to_rows_in_another(
    db: AsyncSession = Depends(get_db),
):
    return await retrieving_rows_from_one_table_that_do_not_correspond(db)


@router.get(
    "/adding-joins-to-a-query-without-interfering-with-other-joins",
    response_model=list[EmpDeptBonusResponse],
)
async def adding_joins_to_a_query_without_interfering_with_other_joins_results(
    db: AsyncSession = Depends(get_db),
):
    return await adding_joins_to_a_query_without_interfering_with_other_joins(db)


@router.get(
    "/determining-whether-two-tables-have-the-same-data",
    response_model=list[EMPViewResponse],
)
async def determining_whether_two_tables_have_the_same_data_result(
    db: AsyncSession = Depends(get_db),
):
    return await determining_whether_two_tables_have_the_same_data(db)


@router.get(
    "/identifying-and-avoiding-cartesian-products",
    response_model=list[EmployeeDeptJoin],
)
async def identifying_and_avoiding_cartesian_products_results(
    db: AsyncSession = Depends(get_db),
):
    return await identifying_and_avoiding_cartesian_products(db)


@router.get(
    "/performing-joins-when-using-aggregates",
    response_model=list[EmpDeptBonusAggregatesResponse],
)
async def performing_joins_when_using_aggregates_results(
    db: AsyncSession = Depends(get_db),
):
    return await performing_joins_when_using_aggregates(db)


@router.get(
    "/performing-outer-joins-when-using-aggregates",
    response_model=list[EmpDeptBonusAggregatesResponse],
)
async def performing_outer_joins_when_using_aggregates_results(
    db: AsyncSession = Depends(get_db),
):
    return await performing_outer_joins_when_using_aggregates(db)


@router.get(
    "/returning-missing-data-from-multiple-tables",
    response_model=list[DEPTEMPResponse],
)
async def returning_missing_data_from_multiple_tables_results(
    db: AsyncSession = Depends(get_db),
):
    return await returning_missing_data_from_multiple_tables(db)


@router.get(
    "/using-nulls-in-operations-and-comparisons",
    response_model=list[EMPCreate],
)
async def using_nulls_in_operations_and_comparisons_resuls(
    db: AsyncSession = Depends(get_db),
):
    return await using_nulls_in_operations_and_comparisons(db)
