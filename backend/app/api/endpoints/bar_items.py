from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.session import get_db
from app.schemas.bar_item import BarItem, BarItemCreate, BarItemUpdate
from app.services import bar_item_service

router = APIRouter()


@router.get("/", response_model=List[BarItem])
def read_bar_items(
    skip: int = 0,
    limit: int = 100,
    category: Optional[str] = None,
    available_only: bool = True,
    db: Session = Depends(get_db),
):
    """
    获取酒柜物品列表。
    """
    # 这里调用服务层函数
    # items = bar_item_service.get_bar_items(db, skip=skip, limit=limit, category=category, available_only=available_only)
    # return items
    return []  # 占位符


@router.get("/{item_id}", response_model=BarItem)
def read_bar_item(item_id: int, db: Session = Depends(get_db)):
    """
    根据ID获取酒柜物品。
    """
    # item = bar_item_service.get_bar_item(db, item_id=item_id)
    # if item is None:
    #     raise HTTPException(status_code=404, detail="酒柜物品未找到")
    # return item
    raise HTTPException(status_code=404, detail="功能尚未实现")


@router.post("/", response_model=BarItem)
def create_bar_item(item: BarItemCreate, db: Session = Depends(get_db)):
    """
    创建新的酒柜物品。
    """
    # return bar_item_service.create_bar_item(db=db, item=item)
    raise HTTPException(status_code=501, detail="功能尚未实现")


@router.put("/{item_id}", response_model=BarItem)
def update_bar_item(item_id: int, item: BarItemUpdate, db: Session = Depends(get_db)):
    """
    更新酒柜物品。
    """
    # db_item = bar_item_service.get_bar_item(db, item_id=item_id)
    # if db_item is None:
    #     raise HTTPException(status_code=404, detail="酒柜物品未找到")
    # return bar_item_service.update_bar_item(db=db, db_item=db_item, item=item)
    raise HTTPException(status_code=501, detail="功能尚未实现")


@router.delete("/{item_id}")
def delete_bar_item(item_id: int, db: Session = Depends(get_db)):
    """
    删除酒柜物品。
    """
    # db_item = bar_item_service.get_bar_item(db, item_id=item_id)
    # if db_item is None:
    #     raise HTTPException(status_code=404, detail="酒柜物品未找到")
    # bar_item_service.delete_bar_item(db=db, item_id=item_id)
    # return {"message": "酒柜物品已删除"}
    raise HTTPException(status_code=501, detail="功能尚未实现")