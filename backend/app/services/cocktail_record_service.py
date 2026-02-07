from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.cocktail_record import CocktailRecord
from app.schemas.cocktail_record import CocktailRecordCreate, CocktailRecordUpdate


def get_cocktail_records(db: Session, skip: int = 0, limit: int = 100) -> List[CocktailRecord]:
    """
    获取调酒记录列表。
    """
    return db.query(CocktailRecord).offset(skip).limit(limit).all()


def get_cocktail_record(db: Session, record_id: int) -> Optional[CocktailRecord]:
    """
    根据ID获取调酒记录。
    """
    return db.query(CocktailRecord).filter(CocktailRecord.id == record_id).first()


def create_cocktail_record(db: Session, record: CocktailRecordCreate) -> CocktailRecord:
    """
    创建调酒记录。
    """
    db_record = CocktailRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record


def update_cocktail_record(db: Session, db_record: CocktailRecord, record: CocktailRecordUpdate) -> CocktailRecord:
    """
    更新调酒记录。
    """
    update_data = record.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_record, field, value)
    
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record


def delete_cocktail_record(db: Session, record_id: int) -> None:
    """
    删除调酒记录。
    """
    db_record = get_cocktail_record(db, record_id=record_id)
    if db_record:
        db.delete(db_record)
        db.commit()