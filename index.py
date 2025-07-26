from fastapi import FastAPI  # Import the router
from .backend_fast_api import router

from pydantic import BaseModel

app = FastAPI()

# Include the router
app.include_router(router.router)
# app.include_router(items.router)


# from fastapi import FastAPI, Request
# import time

# app = FastAPI()


# # ✅ MIDDLEWARE: Logs request time
# @app.middleware("http")
# async def log_time(request: Request, call_next):
#     start = time.time()
#     response = await call_next(request)
#     duration = time.time() - start
#     print(f"{request.method} {request.url.path} took {duration:.4f} seconds")
#     return response


# # ✅ SIMPLE GET REQUEST
# @app.get("/")
# async def hello():
#     return {"message": "Hello, FastAPI!"}
