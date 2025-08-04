from fastapi import FastAPI, Request
from .backend_fast_api import router
from fastapi.middleware.cors import CORSMiddleware
from .backend_fast_api import auth

from fastapi.responses import JSONResponse
from .backend_fast_api.auth import verify_token

app = FastAPI()


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
