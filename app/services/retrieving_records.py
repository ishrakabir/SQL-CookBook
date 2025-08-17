from sqlalchemy import select, literal, or_, case, func
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.emp import EMP
from typing import List

from app.schemas.emp import (
    EMPResponse,
    NameResponse,
    EmployeeInfo,
    SalaryCommissionResponse,
    EmployeeMessageResponse,
    EmployeStatusResponse,
)


async def get_low_salary_employees(db: AsyncSession, max_salary: int) -> List[EMP]:
    stmt = select(EMP).where(EMP.sal < max_salary)
    result = await db.execute(stmt)
    return result.scalars().all()


async def finding_rows_that_satisfy_multiple_conditions(
    db: AsyncSession, dept_no: int
) -> list[EMPResponse]:
    stmt = select(EMP).where(
        or_(
            EMP.deptno == dept_no,
            EMP.comm.isnot(None),
        )
    )
    result = await db.execute(stmt)

    return result.scalars().all()


async def retrieving_a_subset_of_column(db: AsyncSession) -> list[NameResponse]:
    stmt = select(EMP.ename)
    result = await db.execute(stmt)
    names = result.scalars().all()
    return [{"name": n} for n in names]


async def providing_meaningful_names(db: AsyncSession) -> list[EmployeeInfo]:
    stmt = select(
        EMP.ename.label("name"), EMP.deptno.label("department_no"), EMP.sal.label("salary")
    )
    result = await db.execute(stmt)
    return result.mappings().all()


async def referencing_an_aliased_column_in_the_where_clause(
    db: AsyncSession,
) -> list[SalaryCommissionResponse]:
    subq = select(EMP.sal.label("salary"), EMP.comm.label("commission")).subquery()
    stmt = select(subq).where(subq.c.salary < 5000)
    result = await db.execute(stmt)
    return result.mappings().all()


async def concatenating_column(db: AsyncSession, dept_no: int) -> list[EmployeeMessageResponse]:
    stmt = select((EMP.ename + literal(" works as a ") + EMP.job).label("msg")).where(
        EMP.deptno == dept_no
    )
    result = await db.execute(stmt)
    return result.mappings().all()


async def using_conditional_logic(
    db: AsyncSession,
) -> list[EmployeStatusResponse]:
    stmt = select(
        EMP.ename,
        EMP.sal,
        (case((EMP.sal <= 2000, "UNDERPAID"), (EMP.sal >= 4000, "OVERPAID"), else_="Ok")).label(
            "status"
        ),
    )
    result = await db.execute(stmt)
    return result.mappings().all()


async def limiting_the_number(db: AsyncSession, skip: int = 0, limit: int = 5) -> list[EMPResponse]:
    stmt = select(EMP).offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()


async def returning_n_random_records(db: AsyncSession, limit: int = 5) -> list[EMPResponse]:
    stmt = select(EMP).order_by(func.random()).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()


async def finding_null(db: AsyncSession, limit: int = 5) -> list[EMPResponse]:
    stmt = select(EMP).where(EMP.comm.is_(None)).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()


async def transforming_null_into_real(db: AsyncSession, limit: int = 5) -> list[dict]:
    stmt = select(func.coalesce(EMP.comm, 0).label("commission")).limit(limit)
    result = await db.execute(stmt)
    return result.mappings().all()


async def searching_for_patterns(db: AsyncSession, limit: int = 5) -> list[dict]:
    stmt = (
        select(EMP.ename, EMP.job)
        .where(EMP.deptno.in_([10, 20]), or_(EMP.ename.like("%I"), EMP.job.like("%ER")))
        .limit(limit)
    )
    result = await db.execute(stmt)
    return result.mappings().all()
