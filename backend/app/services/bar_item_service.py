from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.bar_item import BarItem
from app.schemas.bar_item import BarItemCreate, BarItemUpdate


def get_bar_items(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    category: Optional[str] = None,
    available_only: bool = True,
) -> List[BarItem]:
    """
    获取酒柜物品列表。
    """
    # 这里实现数据库查询逻辑
    query = db.query(BarItem)
    
    if category:
        query = query.filter(BarItem.category == category)
    
    if available_only:
        query = query.filter(BarItem.is_available == True)
    
    return query.offset(skip).limit(limit).all()


def get_bar_item(db: Session, item_id: int) -> Optional[BarItem]:
    """
    根据ID获取酒柜物品。
    """
    return db.query(BarItem).filter(BarItem.id == item_id).first()


def create_bar_item(db: Session, item: BarItemCreate) -> BarItem:
    """
    创建新的酒柜物品。
    """
    db_item = BarItem(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_bar_item(db: Session, db_item: BarItem, item: BarItemUpdate) -> BarItem:
    """
    更新酒柜物品。
    """
    update_data = item.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_item, field, value)
    
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_bar_item(db: Session, item_id: int) -> None:
    """
    删除酒柜物品。
    """
    db_item = get_bar_item(db, item_id=item_id)
    if db_item:
        db.delete(db_item)
        db.commit()