from typing import List, Optional
from sqlalchemy import select, func, case
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.emp import EMP
from app.schemas.emp import EmployeeSortedSalary, EmployeeSortedJob, EMPCreate
from app.models.views import V
from app.schemas.views import VResponse


async def returning_query_results(
    db: AsyncSession, dept_no: Optional[int]
) -> List[EmployeeSortedSalary]:
    stmt = select(EMP.sal, EMP.ename, EMP.deptno)
    if dept_no is not None:
        stmt = stmt.where(EMP.deptno == dept_no)
    stmt = stmt.order_by(EMP.sal.asc())
    result = await db.execute(stmt)
    return result.mappings().all()


async def sorting_by_multiple_fields(
    db: AsyncSession, dept_no: Optional[int]
) -> List[EmployeeSortedSalary]:
    stmt = select(EMP.sal, EMP.ename, EMP.deptno)
    if dept_no is not None:
        stmt = stmt.where(EMP.deptno == dept_no)
    stmt = stmt.order_by(EMP.sal.asc(), EMP.deptno.asc())
    result = await db.execute(stmt)
    return result.mappings().all()


async def sorting_by_substrings(db: AsyncSession) -> List[EmployeeSortedJob]:
    order_expr = func.right(EMP.job, 2)
    stmt = select(EMP)

    stmt = stmt.order_by(order_expr.asc())
    result = await db.execute(stmt)
    return result.scalars().all()


async def sorting_mixed_alphanumeric(db: AsyncSession) -> List[VResponse]:
    col = V.data
    expr = func.replace(
        col, func.replace(func.translate(col, "0123456789", "##########"), "#", ""), ""
    )
    stmt = select(V).order_by(expr.asc())

    result = await db.execute(stmt)
    return result.scalars().all()


async def dealing_with_nulls_when_sorting(db: AsyncSession) -> List[EMPCreate]:
    stmt = select(EMP).order_by(EMP.comm.asc().nulls_first())

    result = await db.execute(stmt)
    return result.scalars().all()


async def sorting_on_a_data_dependent_key(db: AsyncSession) -> List[EMP]:
    stmt = select(EMP).order_by(case((EMP.job == "SALESMAN", EMP.comm), else_=EMP.sal).asc())

    result = await db.execute(stmt)
    return result.scalars().all()
