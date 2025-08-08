from fastapi import FastAPI, Request
from .backend_fast_api import router
from fastapi.middleware.cors import CORSMiddleware
from .backend_fast_api import auth

from fastapi.responses import JSONResponse
from .backend_fast_api.auth import verify_token

import asyncio
from contextlib import asynccontextmanager

from .backend_fast_api.background_task import generate_image


async def repeat_task():
    try:
        while True:
            await generate_image(workers=3)
            print("i am task")
            await asyncio.sleep(10)
    except asyncio.CancelledError:
        print("Task might be cancelled")


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("App is starting...")
    task = asyncio.create_task(repeat_task())
    print("i am task is lifespan")
    yield
    task.cancel()
    print(" App is stopping...")


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def check_user_token(request: Request, call_next):
    public_paths = [
        "/token",
        "/register",
        "/public",
        "/docs",
        "/openapi.json",
    ]

    if request.method == "OPTIONS":
        return await call_next(request)

    if any(request.url.path.startswith(p) for p in public_paths):
        return await call_next(request)

    print("headers data", request.headers)
    auth_header = request.headers.get("Authorization")
    print(auth_header, "auth_header")
    if not auth_header or not auth_header.startswith("Bearer "):
        return JSONResponse(
            status_code=401, content={"detail": "Unauthorized: Missing token"}
        )

    token = auth_header.split(" ")[1]
    print("i ma from backed token", token)

    try:
        verify_token(token)
    except Exception:
        return JSONResponse(
            status_code=401,
            content={"detail": "Unauthorized: Invalid or expired token"},
        )

    return await call_next(request)


app.include_router(auth.router)

app.include_router(router.router)


@app.get("/dashboard")
async def dashboard():
    return {"message": "Welcome to your dashboard!"}


@app.get("/public")
async def public():
    return {"message": "This is a public page. No token needed."}


# # from fastapi import FastAPI
# # import asyncio
# # from contextlib import asynccontextmanager


# # async def hi():
# #     global num
# #     while True:
# #         num += 1
# #         print("welcome to Konic")
# #         print("asdjhj")
# #         await asyncio.sleep(2)


# # @asynccontextmanager
# # async def lifespan(app: FastAPI):
# #     task = asyncio.create_task(hi())
# #     yield
# #     task.cancel()
# #     try:
# #         await task
# #     except asyncio.CancelledError:
# #         print("Task cancelled")


# # app = FastAPI(lifespan=lifespan)


# # from fastapi import FastAPI
# # import asyncio
# # from contextlib import asynccontextmanager

# # from contextlib import contextmanager

# # from .database_configaration.un_matched_records_table import UNMATCHEDRECORDS
# # from .database_configaration.database_connection import get_session
# # from sqlmodel import select


# # @contextmanager
# # def get_db_session():
# #     yield from get_session()


# # async def repeat_task():
# #     while True:
# #         # 🔁 Sync DB session inside async function (acceptable with care)
# #         with get_db_session() as session:
# #             statement = select(UNMATCHEDRECORDS)
# #             dishes = session.exec(statement).all()
# #             dishes_with_id = [{"id": i.id, "name": i.name} for i in dishes]

# #             if dishes_with_id:
# #                 print(dishes_with_id)

# #         # 💤 Wait between DB reads
# #         await asyncio.sleep(2)

# #         print("Function running...")
# #         print("This is sai")
# #         await asyncio.sleep(2)  # Optional: Add delay if needed


# # @asynccontextmanager
# # async def lifespan(app: FastAPI):
# #     print("🔌 App is starting...")
# #     task = asyncio.create_task(repeat_task())
# #     yield
# #     print("❌ App is stopping...")
# #     task.cancel()
# #     try:
# #         await task
# #     except asyncio.CancelledError:
# #         print("✅ Background task cancelled.")


# # app = FastAPI(lifespan=lifespan)


# # @app.get("/")
# # async def root():
# #     return {"message": "Hello from FastAPI!"}
