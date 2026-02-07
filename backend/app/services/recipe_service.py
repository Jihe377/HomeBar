from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.recipe import Recipe, RecipeIngredient, Tag
from app.models.bar_item import BarItem
from app.schemas.recipe import RecipeCreate, RecipeUpdate, RecipeWithAvailability


def get_recipes(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    difficulty: Optional[str] = None,
    is_iba_official: Optional[bool] = None,
    tag_id: Optional[int] = None,
) -> List[Recipe]:
    """
    获取配方列表。
    """
    query = db.query(Recipe)
    
    if difficulty:
        query = query.filter(Recipe.difficulty == difficulty)
    
    if is_iba_official is not None:
        query = query.filter(Recipe.is_iba_official == is_iba_official)
    
    if tag_id:
        query = query.join(Recipe.tags).filter(Tag.id == tag_id)
    
    return query.offset(skip).limit(limit).all()


def get_recipe(db: Session, recipe_id: int) -> Optional[Recipe]:
    """
    根据ID获取配方。
    """
    return db.query(Recipe).filter(Recipe.id == recipe_id).first()


def create_recipe(db: Session, recipe: RecipeCreate) -> Recipe:
    """
    创建新配方。
    """
    # 这里实现创建配方的逻辑，包括处理成分和标签
    db_recipe = Recipe(
        name=recipe.name,
        description=recipe.description,
        instructions=recipe.instructions,
        glassware=recipe.glassware,
        difficulty=recipe.difficulty,
        is_public=recipe.is_public,
        is_iba_official=recipe.is_iba_official,
        source=recipe.source,
        prep_time=recipe.prep_time,
        total_time=recipe.total_time,
    )
    
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    
    # 添加成分
    for ingredient_data in recipe.ingredients:
        ingredient = RecipeIngredient(
            recipe_id=db_recipe.id,
            bar_item_id=ingredient_data.bar_item_id,
            name=ingredient_data.name,
            quantity=ingredient_data.quantity,
            unit=ingredient_data.unit,
            note=ingredient_data.note,
        )
        db.add(ingredient)
    
    # 添加标签
    if recipe.tag_ids:
        tags = db.query(Tag).filter(Tag.id.in_(recipe.tag_ids)).all()
        db_recipe.tags.extend(tags)
    
    db.commit()
    db.refresh(db_recipe)
    return db_recipe


def update_recipe(db: Session, db_recipe: Recipe, recipe: RecipeUpdate) -> Recipe:
    """
    更新配方。
    """
    update_data = recipe.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_recipe, field, value)
    
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe


def delete_recipe(db: Session, recipe_id: int) -> None:
    """
    删除配方。
    """
    db_recipe = get_recipe(db, recipe_id=recipe_id)
    if db_recipe:
        db.delete(db_recipe)
        db.commit()


def check_recipe_availability(db: Session, recipe: Recipe) -> RecipeWithAvailability:
    """
    检查配方是否可用现有材料制作。
    """
    missing_ingredients = []
    can_make = True
    
    for ingredient in recipe.ingredients:
        if ingredient.bar_item_id:
            bar_item = db.query(BarItem).filter(
                BarItem.id == ingredient.bar_item_id,
                BarItem.is_available == True
            ).first()
            
            if not bar_item:
                missing_ingredients.append(ingredient)
                can_make = False
            elif bar_item.current_volume and bar_item.current_volume < ingredient.quantity:
                missing_ingredients.append(ingredient)
                can_make = False
        else:
            # 如果没有关联bar_item_id，假设该成分是通用物品（如冰块、柠檬片）
            # 这里可以添加逻辑检查通用物品的库存
            pass
    
    # 创建响应对象
    from app.schemas.recipe import RecipeWithAvailability
    return RecipeWithAvailability(
        **recipe.__dict__,
        can_make=can_make,
        missing_ingredients=missing_ingredients,
    )


def get_available_recipes(db: Session, skip: int = 0, limit: int = 100) -> List[RecipeWithAvailability]:
    """
    获取可用现有材料制作的配方列表。
    """
    recipes = get_recipes(db, skip=skip, limit=limit)
    result = []
    
    for recipe in recipes:
        availability = check_recipe_availability(db, recipe)
        if availability.can_make:
            result.append(availability)
    
    return result