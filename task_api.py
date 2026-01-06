from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    title: str
    completed: bool = False

tasks = []

@app.post("/tasks")
def add_task(task: Task):
    tasks.append(task)
    return {"status": "added", "task": task}

@app.get("/tasks")
def list_tasks():
    return tasks

@app.put("/tasks/{index}")
def complete_task(index: int):
    if 0 <= index < len(tasks):
        tasks[index].completed = True
        return {"status": "completed", "task": tasks[index]}
    return {"error": "Invalid index"}

@app.delete("/tasks/{index}")
def delete_task(index: int):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        return {"status": "deleted", "task": removed}
    return {"error": "Invalid index"}
@app.get("/")
def root():
    return {"message": "Task API running"}