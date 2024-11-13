from pydantic import BaseModel
from typing import Optional

# User Schemas
class UserCreate(BaseModel):
    email: str
    full_name: str
    password: str
    role: str = "user"

class UserResponse(BaseModel):
    id: int
    email: str
    full_name: str
    role: str

    class Config:
        orm_mode = True

class LoginRequest(BaseModel):
    email: str
    password: str
    
# Task Schemas
class TaskCreate(BaseModel):
    title: str
    description: str

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
    owner_id: int

    class Config:
        orm_mode = True
