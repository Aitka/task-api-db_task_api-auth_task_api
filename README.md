# task-api
# Task Management API (FastAPI)

A simple but production-ready REST API built with **Python + FastAPI** that supports:

- User registration and login (JWT authentication)
- Secure password hashing
- Task CRUD operations
- Persistent storage with SQLite
- Interactive API documentation

This project is built as a portfolio backend application demonstrating modern API design and authentication.

---

## 🚀 Features

- User registration and login
- Password hashing using PBKDF2 (secure and compatible with Python 3.14+)
- JWT token authentication
- Create / Read / Update / Delete tasks
- SQLite database persistence
- Interactive API docs via Swagger UI

---

## 🧱 Tech Stack

| Layer | Technology |
|------|------------|
Backend | Python 3.14 |
API Framework | FastAPI |
Database | SQLite |
ORM | SQLModel |
Authentication | JWT (python-jose) |
Password Hashing | Passlib (PBKDF2-SHA256) |
Server | Uvicorn |

---

## ⚙️ How to Run

### 1. Clone repository

```bash
git clone <your-repo-url>
cd <your-repo-name>
