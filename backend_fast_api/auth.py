from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta, timezone

# import time

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form,
    Query,
    Depends,
    HTTPException,
    status,
)
from jose import JWTError, jwt

from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr
from sqlmodel import select
from contextlib import contextmanager
import uuid

from ..database_configaration.user_models import User
from ..database_configaration.database_connection import get_session

router = APIRouter()


@contextmanager
def get_db_session():
    yield from get_session()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


SECRET_KEY = "aaf4cc47d14aa9f80b7eafd3fe8d37ffe45c4b1aaefad0c7b70dfd4360ef2bc613f2b8a83cfab54f5c61cf4667f4b696aa851f57de2365923dd53ae9b87fb8ef"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 40


class UserModel(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserResponseModel(BaseModel):
    id: str
    name: str
    email: EmailStr

    class Config:
        orm_mode = True


def create_user(user: UserModel):
    with get_db_session() as session:
        hashed_password = pwd_context.hash(user.password)
        db_user = User(
            id=str(uuid.uuid4()),
            name=user.name,
            email=user.email,
            hashed_password=hashed_password,
        )
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user


def get_user_by_email(email: str):
    with get_db_session() as session:
        statement = select(User).where(User.email == email)
        result = session.exec(statement).first()
        return result


@router.post("/register", response_model=UserResponseModel)
def register_user(user: UserModel):
    db_user = get_user_by_email(user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(user)


def authenticate_user(email: EmailStr, password: str):
    with get_db_session() as session:
        statement = select(User).where(User.email == email)
        user = session.exec(statement).first()

        if not user:
            return None

        if not pwd_context.verify(password, user.hashed_password):
            return None
        return user


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(days=7)

    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")


def get_current_user(token: str = Depends(oauth2_scheme)):
    return verify_token(token)
