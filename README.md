<!-- PROJECT SHIELDS -->
<p align="center">
  <img src="https://img.shields.io/badge/PostgreSQL-✔-336791?logo=postgresql&logoColor=white" alt="Postgres" />
  <img src="https://img.shields.io/badge/FastAPI-⚡-009688?logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/SQLAlchemy-async-ff5533?logo=python&logoColor=white" alt="SQLAlchemy" />
</p>

<h1 align="center">
  📘 SQL Cookbook Solutions  
  <br>
  <sub>PostgreSQL Queries • FastAPI Endpoints • Async SQLAlchemy</sub>
</h1>

---

## ✨ Features

- ✅ **PostgreSQL** queries implemented & tested  
- ✅ **FastAPI** endpoints with `Swagger` auto-docs  
- ✅ **Async SQLAlchemy** for modern, non-blocking query handling  
- ✅ **Chapter-by-chapter** organization mirroring the **SQL Cookbook**  
- ✅ Clean modular structure: `schemas`, `services`, `routers`  
- ✅ Practical **real-world API integration examples**

---

## 🚀 Getting Started

Clone, configure, and run the project:

1. Clone
git clone https://github.com/<your-username>/sql-cookbook.git
cd sql-cookbook

2. (Optional) Setup virtual environment
python -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Configure .env (at project root)
echo "DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/dbname" > .env

5. Run API
uvicorn main:app --reload


📖 Docs available at: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**  

---

## 📚 Chapters Implemented

Each chapter is **self-contained** with models, services, and routers.  
This makes it easy to test SQL concepts via **live API endpoints**.

| #  | Chapter Title                          | Status   |
|----|----------------------------------------|----------|
| 1  | Retrieving Records                     | ✅ Done |
| 2  | Sorting Query Results                  | ✅ Done |
| 3  | Working with Multiple Tables           | 🚧 In Progress |
| 4  | Inserting, Updating, and Deleting      | ⏳ To Do |
| 5  | Metadata Queries                       | ⏳ To Do |
| 6  | Working with Strings                   | ⏳ To Do |
| 7  | Working with Numbers                   | ⏳ To Do |
| 8  | Date Arithmetic                        | ⏳ To Do |
| 9  | Date Manipulation                      | ⏳ To Do |
| 10 | Working with Ranges                    | ⏳ To Do |
| 11 | Advanced Searching                     | ⏳ To Do |
| 12 | Reporting and Reshaping                | ⏳ To Do |
| 13 | Hierarchical Queries                   | ⏳ To Do |
| 14 | Odds ‘n’ Ends                          | ⏳ To Do |
| 15 | Window Function Refresher              | ⏳ To Do |
| 16 | Common Table Expressions (CTEs)        | ⏳ To Do |
| 17 | Index                                  | ⏳ To Do |


---




---

## ⚡ Example Endpoint Workflow

- **Chapter:** Retrieving Records  
- **API Endpoint:** `GET /chapter1/employees`  
- **Process:**
  1. FastAPI router calls → `chapter1_router.py`  
  2. Router delegates → `chapter1_service.py`  
  3. Service executes → `async SQLAlchemy session` query  
  4. Results validated via → `chapter1_schema.py`  
  5. Response returned as → clean JSON  

---

## 🤝 Contributing

We welcome contributions! 🎉

1. Fork & clone the repo  
2. Create a feature branch per chapter/topic  
3. Write clean modular code (`schemas`, `services`, `routers`)  
4. Run & add tests if possible  
5. Open a PR with **conventional commit messages**

---


## 🌍 Vision

A **practical, navigable SQL reference**:  
By working **chapter-by-chapter** through the *SQL Cookbook*, with real **PostgreSQL queries** & **FastAPI playground endpoints**,  
you don’t just read solutions—you **run them** in production-ready patterns. 🚀

---

<p align="center">⭐ If you find this project useful, consider giving it a star on GitHub! ⭐</p>

