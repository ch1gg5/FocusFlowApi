from fastapi import FastAPI
from routers import auth, tasks, categories, sessions

app = FastAPI()

app.include_router(auth.router)

app.include_router(categories.router)

app.include_router(tasks.router)

app.include_router(sessions.router)

