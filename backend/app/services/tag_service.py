from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.recipe import Tag
from app.schemas.recipe import TagCreate


def get_tags(db: Session, skip: int = 0, limit: int = 100) -> List[Tag]:
    """
    获取标签列表。
    """
    return db.query(Tag).offset(skip).limit(limit).all()


def get_tag(db: Session, tag_id: int) -> Optional[Tag]:
    """
    根据ID获取标签。
    """
    return db.query(Tag).filter(Tag.id == tag_id).first()


def create_tag(db: Session, tag: TagCreate) -> Tag:
    """
    创建标签。
    """
    db_tag = Tag(**tag.dict())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag


def delete_tag(db: Session, tag_id: int) -> None:
    """
    删除标签。
    """
    db_tag = get_tag(db, tag_id=tag_id)
    if db_tag:
        db.delete(db_tag)
        db.commit()