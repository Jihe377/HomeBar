from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.shopping import ShoppingItem, ShoppingStatus
from app.models.recipe import Recipe, RecipeIngredient
from app.models.bar_item import BarItem
from app.schemas.shopping import ShoppingItemCreate, ShoppingItemUpdate


def get_shopping_items(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    status: str = "pending",
) -> List[ShoppingItem]:
    """
    获取购物清单项目列表。
    """
    query = db.query(ShoppingItem)
    
    if status:
        query = query.filter(ShoppingItem.status == ShoppingStatus(status))
    
    return query.offset(skip).limit(limit).all()


def get_shopping_item(db: Session, item_id: int) -> Optional[ShoppingItem]:
    """
    根据ID获取购物清单项目。
    """
    return db.query(ShoppingItem).filter(ShoppingItem.id == item_id).first()


def create_shopping_item(db: Session, item: ShoppingItemCreate) -> ShoppingItem:
    """
    创建购物清单项目。
    """
    db_item = ShoppingItem(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def create_shopping_items_from_recipe(db: Session, recipe: Recipe) -> List[ShoppingItem]:
    """
    根据配方创建购物清单项目（添加缺失的材料）。
    """
    shopping_items = []
    
    for ingredient in recipe.ingredients:
        if ingredient.bar_item_id:
            bar_item = db.query(BarItem).filter(
                BarItem.id == ingredient.bar_item_id
            ).first()
            
            if not bar_item or not bar_item.is_available or (bar_item.current_volume and bar_item.current_volume < ingredient.quantity):
                # 创建购物清单项目
                shopping_item = ShoppingItem(
                    bar_item_id=ingredient.bar_item_id,
                    name=ingredient.name,
                    quantity=ingredient.quantity,
                    unit=ingredient.unit,
                    notes=f"用于制作 {recipe.name}",
                )
                db.add(shopping_item)
                shopping_items.append(shopping_item)
    
    db.commit()
    return shopping_items


def update_shopping_item(db: Session, db_item: ShoppingItem, item: ShoppingItemUpdate) -> ShoppingItem:
    """
    更新购物清单项目。
    """
    update_data = item.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_item, field, value)
    
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_shopping_item(db: Session, item_id: int) -> None:
    """
    删除购物清单项目。
    """
    db_item = get_shopping_item(db, item_id=item_id)
    if db_item:
        db.delete(db_item)
        db.commit()