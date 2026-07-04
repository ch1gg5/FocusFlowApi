from sqlalchemy.orm import Session
from models.session import Session as StudySession
from models.task import Task
from schemas.session import SessionCreate

def create_session(db: Session, user_id: int, data: SessionCreate):
    # Check if the task exists and belongs to the user
    task = db.query(Task).filter(Task.id == data.task_id, Task.user_id == user_id).first()
    if not task:
        raise ValueError("Task not found or does not belong to the user.")

    if data.duration_minutes <= 0 or data.duration_minutes > 600:
        raise ValueError("Duration must be between 1 and 600 minutes.")

    new_session = StudySession(
        task_id=data.task_id,
        user_id=user_id,
        duration_minutes=data.duration_minutes,
        date=data.date
    )
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session

def get_sessions(db: Session, user_id: int):
    return db.query(StudySession).filter(StudySession.user_id == user_id).all()