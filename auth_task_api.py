from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Field, Session, create_engine, select
from passlib.context import CryptContext
from jose import jwt

SECRET_KEY = "supersecret"
ALGORITHM = "HS256"

app = FastAPI()
engine = create_engine("sqlite:///users_tasks.db", echo=True)
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    password: str

SQLModel.metadata.create_all(engine)

def hash_password(pw: str) -> str:
    return pwd_context.hash(pw)

def verify_password(pw: str, hashed: str) -> bool:
    return pwd_context.verify(pw, hashed)

def create_token(username: str) -> str:
    return jwt.encode({"sub": username}, SECRET_KEY, algorithm=ALGORITHM)

@app.post("/register")
def register(username: str, password: str):
    with Session(engine) as s:
        existing = s.exec(select(User).where(User.username == username)).first()
        if existing:
            raise HTTPException(400, "Username already exists")

        user = User(username=username, password=hash_password(password))
        s.add(user)
        s.commit()
        s.refresh(user)
        return {"status": "registered", "user": user.username}

@app.post("/login")
def login(username: str, password: str):
    with Session(engine) as s:
        user = s.exec(select(User).where(User.username == username)).first()
        if not user:
            raise HTTPException(401, "Invalid credentials")

        if not verify_password(password, user.password):
            raise HTTPException(401, "Invalid credentials")

        token = create_token(user.username)
        return {"token": token}

@app.get("/")
def root():
    return {"message": "Auth API running"}
