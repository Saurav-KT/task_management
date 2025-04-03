from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.database import sessionmanager
from app.routers import tasks
from app.settings.config import DATABASE_URL

# os.environ["PYTHONBREAKPOINT"] = "0"

description = """
Task management API
user will be able to:
* **Create,Update,Delete,Fetch task**.
"""


@asynccontextmanager
async def lifespan(app: FastAPI):
    sessionmanager.init(DATABASE_URL)
    await sessionmanager.init_db()
    yield


app = FastAPI(title="Task management App",description=description, version="0.0.1", lifespan=lifespan, debug=True)
origins = [
    "http://localhost",
    "http://localhost:8080",
]
app.include_router(tasks.router, prefix="/api")

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8084, workers=1)
