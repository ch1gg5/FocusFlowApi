from sqlalchemy.orm import Session
from models.task import Task
from schemas.task import TaskCreate, TaskUpdate

def create_task(db: Session, user_id: int, data: TaskCreate):
    task = Task(
        title=data.title,
        description=data.description,
        priority=data.priority,
        category_id=data.category_id,
        user_id=user_id
    )

    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_tasks(db: Session, user_id: int, completed=None, priority=None, category_id=None):
    query = db.query(Task).filter(Task.user_id == user_id)

    if completed is not None:
        query = query.filter(Task.is_completed == completed)

    if priority:
        query = query.filter(Task.priority == priority)

    if category_id:
        query = query.filter(Task.category_id == category_id)

    return query.all()

def get_task(db: Session, task_id: int, user_id: int):
    return db.query(Task).filter(Task.user_id == user_id, Task.id == task_id).first()

def update_task(db: Session, task_id: int, user_id: int, data: TaskUpdate):
    task = get_task(db, task_id, user_id)
    if not task:
        return None

    for field, value in data.dict(exclude_unset=True).items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: int, user_id: int):
    task = get_task(db, task_id, user_id)
    if not task:
        return None

    db.delete(task)
    db.commit()
    return task


