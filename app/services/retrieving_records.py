from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.emp import EMP
from typing import List
from sqlalchemy import or_


async def get_low_salary_employees(db: AsyncSession, max_salary: int) -> List[EMP]:
    stmt = select(EMP).where(EMP.sal < max_salary)
    result = await db.execute(stmt)
    return result.scalars().all()


async def finding_rows_that_satisfy_multiple_conditions(
    db: AsyncSession, dept_no: int
) -> list[EMP]:
    stmt = select(EMP).where(
        or_(
            EMP.deptno == dept_no,
            EMP.comm.isnot(None),
        )
    )
    result = await db.execute(stmt)

    return result.scalars().all()


async def retrieving_a_subset_of_column(db: AsyncSession) -> list[dict]:
    stmt = select(EMP.ename)
    result = await db.execute(stmt)
    names = result.scalars().all()
    return [{"name": n} for n in names]


async def providing_meaningful_names(db: AsyncSession) -> list[dict]:
    stmt = select(
        EMP.ename.label("name"), EMP.deptno.label("department_no"), EMP.sal.label("salary")
    )
    result = await db.execute(stmt)
    return result.mappings().all()


async def referencing_an_aliased_column_in_the_where_clause(db: AsyncSession) -> list[dict]:
    stmt = select(
        EMP.ename.label("name"), EMP.deptno.label("department_no"), EMP.sal.label("salary")
    )
    result = await db.execute(stmt)
    return result.mappings().all()
