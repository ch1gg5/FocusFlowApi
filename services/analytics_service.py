from sqlalchemy import func
from datetime import datetime, timedelta
from models.session import Session
from models.task import Task
from models.category import Category

def get_total_study_hours(db, user_id: int):
    total_minutes = db.query(
        func.sum(Session.duration_minutes)
    ).filter(Session.user_id == user_id).scalar() or 0

    return {
        "totalHours": round(total_minutes / 60, 2)
    }

def get_category_breakdown(db, user_id: int):
    result = db.query(
        Category.name,
        func.sum(Session.duration_minutes)
    ).join(Task, Task.id == Session.task_id
    ).join(Category, Category.id == Task.category_id
    ).filter(Session.user_id == user_id
    ).group_by(Category.name).all()

    return [
        {
            "category": r[0],
            "totalHours": round(r[1] / 60, 2)
        }
        for r in result
    ]

def get_weekly_productivity(db, user_id: int):
    today = datetime.utcnow()
    week_ago = today - timedelta(days=7)

    result = db.query(
        func.date(Session.date),
        func.sum(Session.duration_minutes)
    ).filter(Session.user_id == user_id,
        Session.date >= week_ago
    ).group_by(func.date(Session.date)).all()

    return [
        {
            "date": r[0],
            "hours": round(r[1] / 60, 2)
        }
        for r in result
    ]

def get_streak(db, user_id: int):
    sessions = db.query(
        func.date(Session.date)
    ).filter(Session.user_id == user_id
    ).distinct().all()

    dates = sorted([s[0] for s in sessions])

    streak = 0
    current = datetime.utcnow().date()

    for i in range(len(dates) - 1, -1, -1):
        if dates[i] == current:
            streak += 1
            current -= timedelta(days=1)
        else:
            break

    return {
        "streak": streak
    }