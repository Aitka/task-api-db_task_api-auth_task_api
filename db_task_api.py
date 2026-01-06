from fastapi import FastAPI
from sqlmodel import SQLModel, Field, Session, create_engine, select

app = FastAPI()
engine = create_engine("sqlite:///tasks.db")

class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    completed: bool = False

SQLModel.metadata.create_all(engine)

@app.post("/tasks")
def add_task(task: Task):
    with Session(engine) as session:
        session.add(task)
        session.commit()
        session.refresh(task)
        return task

@app.get("/tasks")
def list_tasks():
    with Session(engine) as session:
        return session.exec(select(Task)).all()

@app.put("/tasks/{task_id}")
def complete_task(task_id: int):
    with Session(engine) as session:
        task = session.get(Task, task_id)
        if not task:
            return {"error": "Not found"}
        task.completed = True
        session.add(task)
        session.commit()
        return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    with Session(engine) as session:
        task = session.get(Task, task_id)
        if not task:
            return {"error": "Not found"}
        session.delete(task)
        session.commit()
        return {"status": "deleted"}
