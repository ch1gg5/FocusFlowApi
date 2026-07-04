from sqlalchemy.orm import Session
from models.category import Category
from schemas.category import CategoryCreate, CategoryUpdate

def create_category(db: Session, data: CategoryCreate):
    category = Category(name=data.name)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def get_categories(db: Session):
    return db.query(Category).all()

def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def update_category(db: Session, category_id: int, data: CategoryUpdate):
    category = db.query(Category).filter(Category.id == category_id).first()
    if category:
        category.name = data.name
        db.commit()
        db.refresh(category)
    return category

def delete_category(db: Session, category_id: int):
    category = db.query(Category).filter(Category.id == category_id).first()
    if category:
        db.delete(category)
        db.commit()
    return category