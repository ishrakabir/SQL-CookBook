from sqlalchemy.ext.asyncio import AsyncSession
from app.models.dept import DEPT
from app.models.dept_east import DeptEast
from app.models.d import D
from app.schemas.dept import DEPTCreate
from app.schemas.d import DCreate
from sqlalchemy import insert, select


async def inserting_a_new_record(db: AsyncSession, dept_data: DEPTCreate):
    stmt = DEPT(**dept_data.model_dump())
    db.add(stmt)
    await db.commit()
    await db.refresh(stmt)
    return stmt


async def inserting_default_values(db: AsyncSession, dept_data: DCreate):
    if dept_data is not None:
        stmt = D(**dept_data.model_dump())
    else:
        stmt = D()
    db.add(stmt)
    await db.commit()
    await db.refresh(stmt)
    return stmt


async def copying_rows_from_one_table_into_another(db: AsyncSession, locations: list[str]):
    stmt = insert(DeptEast).from_select(
        ["deptno", "dname", "loc"],
        select(DEPT.deptno, DEPT.dname, DEPT.loc).where(DEPT.loc.in_(locations)),
    )
    await db.execute(stmt)
    await db.commit()
    return {"message": f"Copied rows where loc in {locations}"}
