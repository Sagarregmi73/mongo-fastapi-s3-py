from fastapi import FastAPI
from lib.app.adapter.input.api.v1 import routes

app = FastAPI(title="Clean Architecture File Upload")

app.include_router(routes.router, prefix="/api/v1/files")
