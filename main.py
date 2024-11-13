from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from auth import authenticate_user, create_access_token, get_user
from database import SessionLocal
from models import User, Task
from schemas import UserCreate, TaskCreate
from auth import get_password_hash
from typing import List
from pydantic import BaseModel
from dotenv import load_dotenv
import os
app = FastAPI()

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# Load environment variables
load_dotenv()

# Secret key and algorithm for JWT
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# User login
@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email, "role": user.role})
    return {"access_token": access_token, "token_type": "bearer"}

# Get current user
from jose import JWTError, jwt

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        role: str = payload.get("role")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = get_user(db, email=email)
    if user is None:
        raise credentials_exception
    return user

# Role-based access control
def admin_only(current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")

def user_only(current_user: User = Depends(get_current_user)):
    if current_user.role != "user":
        raise HTTPException(status_code=403, detail="User access required")

# Admin can view all users
@app.get("/users", dependencies=[Depends(admin_only)])
def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()

# Admin can delete a user
@app.delete("/users/{user_id}", dependencies=[Depends(admin_only)])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted"}

# Normal user can view tasks assigned to them
@app.get("/tasks", dependencies=[Depends(user_only)])
def get_user_tasks(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(Task).filter(Task.owner_id == current_user.id).all()

# Admin can view all tasks
@app.get("/tasks/admin", dependencies=[Depends(admin_only)])
def get_all_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()
