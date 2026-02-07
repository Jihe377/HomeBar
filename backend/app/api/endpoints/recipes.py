from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.session import get_db
from app.schemas.recipe import Recipe, RecipeCreate, RecipeUpdate, RecipeWithAvailability
from app.services import recipe_service

router = APIRouter()


@router.get("/", response_model=List[Recipe])
def read_recipes(
    skip: int = 0,
    limit: int = 100,
    difficulty: Optional[str] = None,
    is_iba_official: Optional[bool] = None,
    tag_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    """
    获取配方列表。
    """
    # 这里调用服务层函数
    # recipes = recipe_service.get_recipes(db, skip=skip, limit=limit, difficulty=difficulty, is_iba_official=is_iba_official, tag_id=tag_id)
    # return recipes
    return []  # 占位符


@router.get("/{recipe_id}", response_model=Recipe)
def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    """
    根据ID获取配方。
    """
    # recipe = recipe_service.get_recipe(db, recipe_id=recipe_id)
    # if recipe is None:
    #     raise HTTPException(status_code=404, detail="配方未找到")
    # return recipe
    raise HTTPException(status_code=404, detail="功能尚未实现")


@router.post("/", response_model=Recipe)
def create_recipe(recipe: RecipeCreate, db: Session = Depends(get_db)):
    """
    创建新配方。
    """
    # return recipe_service.create_recipe(db=db, recipe=recipe)
    raise HTTPException(status_code=501, detail="功能尚未实现")


@router.put("/{recipe_id}", response_model=Recipe)
def update_recipe(recipe_id: int, recipe: RecipeUpdate, db: Session = Depends(get_db)):
    """
    更新配方。
    """
    # db_recipe = recipe_service.get_recipe(db, recipe_id=recipe_id)
    # if db_recipe is None:
    #     raise HTTPException(status_code=404, detail="配方未找到")
    # return recipe_service.update_recipe(db=db, db_recipe=db_recipe, recipe=recipe)
    raise HTTPException(status_code=501, detail="功能尚未实现")


@router.delete("/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    """
    删除配方。
    """
    # db_recipe = recipe_service.get_recipe(db, recipe_id=recipe_id)
    # if db_recipe is None:
    #     raise HTTPException(status_code=404, detail="配方未找到")
    # recipe_service.delete_recipe(db=db, recipe_id=recipe_id)
    # return {"message": "配方已删除"}
    raise HTTPException(status_code=501, detail="功能尚未实现")


@router.get("/{recipe_id}/availability", response_model=RecipeWithAvailability)
def check_recipe_availability(recipe_id: int, db: Session = Depends(get_db)):
    """
    检查配方是否可用现有材料制作。
    """
    # recipe = recipe_service.get_recipe(db, recipe_id=recipe_id)
    # if recipe is None:
    #     raise HTTPException(status_code=404, detail="配方未找到")
    # availability = recipe_service.check_recipe_availability(db, recipe=recipe)
    # return availability
    raise HTTPException(status_code=501, detail="功能尚未实现")


@router.get("/available/", response_model=List[RecipeWithAvailability])
def get_available_recipes(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    """
    获取可用现有材料制作的配方列表。
    """
    # recipes = recipe_service.get_available_recipes(db, skip=skip, limit=limit)
    # return recipes
    return []  # 占位符