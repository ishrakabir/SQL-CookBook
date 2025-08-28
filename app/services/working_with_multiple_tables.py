from typing import List, Optional
from sqlalchemy import select, union, and_, except_, func, desc, case, outerjoin
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.emp import EMP
from app.models.dept import DEPT
from app.models.emp_bonus import EmpBonus
from app.schemas.emp import EmployeeDeptUnion, EmployeeDeptJoin, EMPCreate
from app.models.views import V2, V3
from app.schemas.views import V2Response
from app.schemas.dept import DEPTResponse, DEPTEMPResponse
from app.schemas.emp_bonus import EmpDeptBonusResponse, EmpDeptBonusAggregatesResponse


async def stacking_one_rowset_atop_another(
    db: AsyncSession, dept_no: Optional[int]
) -> List[EmployeeDeptUnion]:
    subq1 = select(EMP.ename.label("ename_and_dname"), EMP.deptno)
    if dept_no is not None:
        subq1 = subq1.where(EMP.deptno == dept_no)

    subq2 = select(DEPT.dname.label("ename_and_dname"), DEPT.deptno)

    stmt = union(subq1, subq2).order_by("deptno")

    result = await db.execute(stmt)
    return result.mappings().all()


async def combining_related_rows(db: AsyncSession, dept_no: int) -> List[dict]:
    # stmt = select(EMP.ename, DEPT.loc).where(and_(EMP.deptno == DEPT.deptno, EMP.deptno == dept_no))

    # Using `.join()` is better than using `and_` in the where clause because:
    # 1. It explicitly represents the SQL JOIN, making the intent clearer.
    # 2. It allows SQLAlchemy to generate more optimized SQL.
    # 3. Keeps filtering (`where`) separate from joining conditions, improving readability.

    stmt = (
        select(EMP.ename, DEPT.loc)
        .join(DEPT, EMP.deptno == DEPT.deptno)
        .where(EMP.deptno == dept_no)
    )

    result = await db.execute(stmt)
    return result.mappings().all()


async def finding_rows_in_common_tables(db: AsyncSession) -> List[V2Response]:
    stmt = select(EMP.empno, EMP.ename, EMP.sal, EMP.job, EMP.deptno).join(
        V2, and_(EMP.job == V2.job, EMP.sal == V2.sal, EMP.ename == V2.ename)
    )

    result = await db.execute(stmt)
    return result.mappings().all()


async def retrieving_values_that_not_exists(db: AsyncSession) -> List[dict]:
    stmt = except_(select(DEPT.deptno), select(EMP.deptno))
    result = await db.execute(stmt)
    return result.mappings().all()


async def retrieving_rows_from_one_table_that_do_not_correspond(
    db: AsyncSession,
) -> List[EmpDeptBonusResponse]:
    stmt = select(DEPT).outerjoin(EMP, DEPT.deptno == EMP.deptno).where(EMP.deptno.is_(None))

    result = await db.execute(stmt)
    return result.scalars().all()


async def adding_joins_to_a_query_without_interfering_with_other_joins(
    db: AsyncSession,
) -> List[DEPTResponse]:
    stmt = (
        select(EMP.ename, DEPT.loc, EmpBonus.received)
        .join(DEPT, DEPT.deptno == EMP.deptno)
        .outerjoin(EmpBonus, EmpBonus.empno == EMP.empno)
        .order_by(EmpBonus.received)
    )

    result = await db.execute(stmt)
    return result.mappings().all()


async def determining_whether_two_tables_have_the_same_data(
    db: AsyncSession,
) -> List[dict]:
    emp_cte = (
        select(
            EMP.empno,
            EMP.ename,
            EMP.job,
            EMP.mgr,
            EMP.hiredate,
            EMP.sal,
            EMP.comm,
            EMP.deptno,
            func.count().label("cnt"),
        )
        .group_by(
            EMP.empno,
            EMP.ename,
            EMP.job,
            EMP.mgr,
            EMP.hiredate,
            EMP.sal,
            EMP.comm,
            EMP.deptno,
        )
        .cte("emp_cte")
    )

    v3_cte = (
        select(
            V3.empno,
            V3.ename,
            V3.job,
            V3.mgr,
            V3.hiredate,
            V3.sal,
            V3.comm,
            V3.deptno,
            func.count().label("cnt"),
        )
        .group_by(
            V3.empno,
            V3.ename,
            V3.job,
            V3.mgr,
            V3.hiredate,
            V3.sal,
            V3.comm,
            V3.deptno,
        )
        .cte("v3_cte")
    )

    # EXCEPT in both directions
    q1 = except_(select(emp_cte), select(v3_cte))
    q2 = except_(select(v3_cte), select(emp_cte))

    stmt = union(q1, q2).order_by(desc("deptno"))

    result = await db.execute(stmt)
    return result.mappings().all()


async def identifying_and_avoiding_cartesian_products(
    db: AsyncSession,
) -> List[EmployeeDeptJoin]:
    stmt = select(EMP.ename, DEPT.loc).join(DEPT, EMP.deptno == DEPT.deptno).where(EMP.deptno == 10)

    result = await db.execute(stmt)
    return result.mappings().all()


async def performing_joins_when_using_aggregates(
    db: AsyncSession,
) -> List[EmpDeptBonusAggregatesResponse]:
    subq = (
        select(
            EMP.empno,
            EMP.ename,
            EMP.sal,
            EMP.deptno,
            (
                EMP.sal
                * case(
                    (EmpBonus.type == 1, 0.1),
                    (EmpBonus.type == 2, 0.2),
                    (EmpBonus.type == 3, 0.3),
                )
            ).label("bonus"),
        )
        .where(and_(EMP.empno == EmpBonus.empno, EMP.deptno == 10))
        .subquery()
    )

    stmt = select(
        subq.c.deptno,
        func.sum(func.distinct(subq.c.sal)).label("total_sal"),
        func.sum(subq.c.bonus).label("total_bonus"),
    ).group_by(subq.c.deptno)

    result = await db.execute(stmt)
    return result.mappings().all()


async def performing_outer_joins_when_using_aggregates(
    db: AsyncSession,
) -> List[EmpDeptBonusAggregatesResponse]:
    subq = (
        select(
            EMP.empno,
            EMP.ename,
            EMP.sal,
            EMP.deptno,
            (
                EMP.sal
                * case(
                    (EmpBonus.type == 1, 0.1),
                    (EmpBonus.type == 2, 0.2),
                    (EmpBonus.type == 3, 0.3),
                )
            ).label("bonus"),
        )
        .select_from(EMP)
        .outerjoin(EmpBonus, EMP.empno == EmpBonus.empno)
        .where(EMP.deptno == 10)
        .subquery()
    )

    stmt = select(
        subq.c.deptno,
        func.sum(func.distinct(subq.c.sal)).label("total_sal"),
        func.sum(subq.c.bonus).label("total_bonus"),
    ).group_by(subq.c.deptno)

    result = await db.execute(stmt)
    return result.mappings().all()


async def returning_missing_data_from_multiple_tables(
    db: AsyncSession,
) -> List[DEPTEMPResponse]:
    stmt = select(DEPT.deptno, DEPT.dname, EMP.ename).outerjoin(
        EMP, DEPT.deptno == EMP.deptno, full=True
    )

    result = await db.execute(stmt)
    return result.mappings().all()


async def using_nulls_in_operations_and_comparisons(
    db: AsyncSession,
) -> List[EMPCreate]:
    stmt = select(EMP.ename, EMP.sal, EMP.comm).where(
        func.coalesce(EMP.comm, 0) < (select(EMP.comm).where(EMP.ename == "WARD"))
    )

    result = await db.execute(stmt)
    return result.mappings().all()
