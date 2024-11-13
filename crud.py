from sqlalchemy.orm import Session
from models import User, Task
from schemas import UserCreate, TaskCreate, TaskUpdate
from auth import get_password_hash
from fastapi import HTTPException, status
from utils import send_email
# User CRUD
def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password,
        role=user.role,
        is_active=True
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}

def get_all_users(db: Session):
    return db.query(User).all()

# Task CRUD
def create_task(db: Session, task: TaskCreate, owner_id: int):
    db_task = Task(
        title=task.title,
        description=task.description,
        completed=False,
        owner_id=owner_id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    # Send email notification
    user = db.query(User).filter(User.id == owner_id).first()
    subject = "New Task Created"
    message = f"Task '{db_task.title}' has been created."
    send_email(user.email, subject, message)
    return db_task

def get_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

def get_tasks_by_user(db: Session, user_id: int):
    return db.query(Task).filter(Task.owner_id == user_id).all()

def update_task(db: Session, task_id: int, task_update: TaskUpdate):
    task = get_task(db, task_id)
    if task_update.title:
        task.title = task_update.title
    if task_update.description:
        task.description = task_update.description
    if task_update.completed is not None:
        task.completed = task_update.completed
    db.commit()
    db.refresh(task)
     # Send email notification
    user = task.owner
    subject = "Task Updated"
    message = f"Task '{task.title}' has been updated."
    send_email(user.email, subject, message)

    return task

def delete_task(db: Session, task_id: int):
    task = get_task(db, task_id)
    db.delete(task)
    db.commit()
    # Send email notification
    user = task.owner
    subject = "Task Deleted"
    message = f"Task '{task.title}' has been deleted."
    send_email(user.email, subject, message)
    return {"message": "Task deleted successfully"}

def get_all_tasks(db: Session):
    return db.query(Task).all()
