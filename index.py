from fastapi import FastAPI
from .backend_fast_api import router
from fastapi.middleware.cors import CORSMiddleware

4

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router.router)
