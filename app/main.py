from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import retrieving_records

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(retrieving_records.router, prefix="/retrieving-records", tags=["retrieving-records"])
