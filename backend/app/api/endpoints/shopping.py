from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.schemas.shopping import ShoppingItem, ShoppingItemCreate, ShoppingItemUpdate
from app.services import shopping_service

router = APIRouter()


@router.get("/", response_model=List[ShoppingItem])
def read_shopping_items(
    skip: int = 0,
    limit: int = 100,
    status: str = "pending",
    db: Session = Depends(get_db),
):
    """
    获取购物清单项目列表。
    """
    # items = shopping_service.get_shopping_items(db, skip=skip, limit=limit, status=status)
    # return items
    return []  # 占位符


@router.get("/{item_id}", response_model=ShoppingItem)
def read_shopping_item(item_id: int, db: Session = Depends(get_db)):
    """
    根据ID获取购物清单项目。
    """
    # item = shopping_service.get_shopping_item(db, item_id=item_id)
    # if item is None:
    #     raise HTTPException(status_code=404, detail="购物清单项目未找到")
    # return item
    raise HTTPException(status_code=404, detail="功能尚未实现")


@router.post("/", response_model=ShoppingItem)
def create_shopping_item(item: ShoppingItemCreate, db: Session = Depends(get_db)):
    """
    创建购物清单项目。
    """
    # return shopping_service.create_shopping_item(db=db, item=item)
    raise HTTPException(status_code=501, detail="功能尚未实现")


@router.post("/from-recipe/{recipe_id}", response_model=List[ShoppingItem])
def create_shopping_items_from_recipe(recipe_id: int, db: Session = Depends(get_db)):
    """
    根据配方创建购物清单项目（添加缺失的材料）。
    """
    # recipe = recipe_service.get_recipe(db, recipe_id=recipe_id)
    # if recipe is None:
    #     raise HTTPException(status_code=404, detail="配方未找到")
    # items = shopping_service.create_shopping_items_from_recipe(db, recipe=recipe)
    # return items
    raise HTTPException(status_code=501, detail="功能尚未实现")


@router.put("/{item_id}", response_model=ShoppingItem)
def update_shopping_item(item_id: int, item: ShoppingItemUpdate, db: Session = Depends(get_db)):
    """
    更新购物清单项目。
    """
    # db_item = shopping_service.get_shopping_item(db, item_id=item_id)
    # if db_item is None:
    #     raise HTTPException(status_code=404, detail="购物清单项目未找到")
    # return shopping_service.update_shopping_item(db=db, db_item=db_item, item=item)
    raise HTTPException(status_code=501, detail="功能尚未实现")


@router.delete("/{item_id}")
def delete_shopping_item(item_id: int, db: Session = Depends(get_db)):
    """
    删除购物清单项目。
    """
    # db_item = shopping_service.get_shopping_item(db, item_id=item_id)
    # if db_item is None:
    #     raise HTTPException(status_code=404, detail="购物清单项目未找到")
    # shopping_service.delete_shopping_item(db=db, item_id=item_id)
    # return {"message": "购物清单项目已删除"}
    raise HTTPException(status_code=501, detail="功能尚未实现")