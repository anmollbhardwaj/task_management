from fastapi import FastAPI
from src.utils.db import engine,Base
from src.tasks.router import task_routes
Base.metadata.create_all(engine)

app = FastAPI(title="this is my task management app!")
app.include_router(task_routes)




