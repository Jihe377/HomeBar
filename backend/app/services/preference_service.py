from sqlalchemy.orm import Session
from typing import Optional

from app.models.preference import TastePreference
from app.schemas.preference import TastePreferenceCreate, TastePreferenceUpdate


def get_preference(db: Session, session_id: str) -> Optional[TastePreference]:
    """
    获取口味偏好。
    """
    return db.query(TastePreference).filter(TastePreference.session_id == session_id).first()


def create_preference(db: Session, preference: TastePreferenceCreate) -> TastePreference:
    """
    创建口味偏好。
    """
    db_preference = TastePreference(**preference.dict())
    db.add(db_preference)
    db.commit()
    db.refresh(db_preference)
    return db_preference


def update_preference(db: Session, db_preference: TastePreference, preference: TastePreferenceUpdate) -> TastePreference:
    """
    更新口味偏好。
    """
    update_data = preference.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_preference, field, value)
    
    db.add(db_preference)
    db.commit()
    db.refresh(db_preference)
    return db_preference


def delete_preference(db: Session, session_id: str) -> None:
    """
    删除口味偏好。
    """
    db_preference = get_preference(db, session_id=session_id)
    if db_preference:
        db.delete(db_preference)
        db.commit()