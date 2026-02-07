from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum
from datetime import datetime

from app.schemas.base import BaseSchema, TimestampSchema


class DifficultyLevel(str, Enum):
    """配方难度级别"""
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class RecipeIngredientBase(BaseSchema):
    """配方成分基础模式"""
    bar_item_id: Optional[int] = Field(None, description="酒柜物品ID")
    name: str = Field(..., min_length=1, max_length=100, description="成分名称")
    quantity: float = Field(..., ge=0, description="数量")
    unit: str = Field(..., min_length=1, max_length=20, description="单位")
    note: Optional[str] = Field(None, max_length=200, description="备注")


class RecipeIngredientCreate(RecipeIngredientBase):
    """创建配方成分模式"""
    pass


class RecipeIngredient(RecipeIngredientBase):
    """配方成分响应模式"""
    id: int
    recipe_id: int


class RecipeBase(BaseSchema):
    """配方基础模式"""
    name: str = Field(..., min_length=1, max_length=200, description="配方名称")
    description: Optional[str] = Field(None, description="描述")
    instructions: str = Field(..., min_length=1, description="制作步骤")
    glassware: Optional[str] = Field(None, max_length=100, description="所需杯具")
    difficulty: DifficultyLevel = Field(default=DifficultyLevel.MEDIUM, description="难度")
    is_public: bool = Field(default=True, description="是否公开")
    is_iba_official: bool = Field(default=False, description="是否是IBA官方配方")
    source: Optional[str] = Field(None, max_length=200, description="来源")
    prep_time: Optional[int] = Field(None, ge=0, description="准备时间（分钟）")
    total_time: Optional[int] = Field(None, ge=0, description="总时间（分钟）")


class RecipeCreate(RecipeBase):
    """创建配方模式"""
    ingredients: List[RecipeIngredientCreate] = Field(default_factory=list, description="成分列表")
    tag_ids: Optional[List[int]] = Field(None, description="标签ID列表")


class RecipeUpdate(BaseSchema):
    """更新配方模式"""
    name: Optional[str] = Field(None, min_length=1, max_length=200, description="配方名称")
    description: Optional[str] = Field(None, description="描述")
    instructions: Optional[str] = Field(None, min_length=1, description="制作步骤")
    glassware: Optional[str] = Field(None, max_length=100, description="所需杯具")
    difficulty: Optional[DifficultyLevel] = Field(None, description="难度")
    is_public: Optional[bool] = Field(None, description="是否公开")
    is_iba_official: Optional[bool] = Field(None, description="是否是IBA官方配方")
    source: Optional[str] = Field(None, max_length=200, description="来源")
    prep_time: Optional[int] = Field(None, ge=0, description="准备时间（分钟）")
    total_time: Optional[int] = Field(None, ge=0, description="总时间（分钟）")


class RecipeInDB(RecipeBase, TimestampSchema):
    """数据库中的配方模式"""
    id: int
    rating: float = Field(default=0.0, description="平均评分")
    rating_count: int = Field(default=0, description="评分次数")


class Recipe(RecipeInDB):
    """配方响应模式"""
    ingredients: List[RecipeIngredient] = Field(default_factory=list, description="成分列表")
    tags: List["Tag"] = Field(default_factory=list, description="标签列表")


class RecipeWithAvailability(Recipe):
    """包含可用性信息的配方模式"""
    can_make: bool = Field(..., description="是否可用现有材料制作")
    missing_ingredients: List[RecipeIngredient] = Field(default_factory=list, description="缺失的成分")


class TagBase(BaseSchema):
    """标签基础模式"""
    name: str = Field(..., min_length=1, max_length=50, description="标签名称")
    color: Optional[str] = Field(None, max_length=7, description="颜色代码")


class TagCreate(TagBase):
    """创建标签模式"""
    pass


class Tag(TagBase):
    """标签响应模式"""
    id: int


# 重建模型以解析前向引用
Recipe.model_rebuild()