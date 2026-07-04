from pydantic import BaseModel
from datetime import datetime

class SessionCreate(BaseModel):
    task_id: int
    duration_minutes: int
    date: datetime

class SessionResponse(BaseModel):
    id: int
    task_id: int
    duration_minutes: int
    date: datetime

    class Config:
        from_attributes = True
