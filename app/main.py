from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import retrieving_records, sorting_query_results, working_with_multiple_tables

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    retrieving_records.router, prefix="/retrieving-records", tags=["retrieving-records"]
)
app.include_router(
    sorting_query_results.router, prefix="/sorting-query-results", tags=["sorting-query-results"]
)
app.include_router(
    working_with_multiple_tables.router,
    prefix="/working-with-multiple-tables",
    tags=["working-with-multiple-tables"],
)
