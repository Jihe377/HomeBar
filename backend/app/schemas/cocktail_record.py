from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from enum import Enum
from datetime import datetime

from app.schemas.base import BaseSchema, TimestampSchema


class TasteRating(str, Enum):
    """口味评价"""
    TOO_SWEET = "too_sweet"
    TOO_SOUR = "too_sour"
    TOO_BITTER = "too_bitter"
    TOO_STRONG = "too_strong"
    TOO_WEAK = "too_weak"
    PERFECT = "perfect"
    GOOD = "good"
    OK = "ok"
    BAD = "bad"


class CocktailRecordBase(BaseSchema):
    """调酒记录基础模式"""
    recipe_id: int = Field(..., description="配方ID")
    tag_id: Optional[int] = Field(None, description="标签ID")
    
    # 实际使用的分量记录
    actual_ingredients: Optional[Dict[str, Any]] = Field(None, description="实际使用的成分和分量")
    
    # 评价
    taste_rating: Optional[TasteRating] = Field(None, description="口味评价")
    personal_rating: Optional[int] = Field(None, ge=1, le=5, description="个人评分（1-5）")
    notes: Optional[str] = Field(None, description="备注")


class CocktailRecordCreate(CocktailRecordBase):
    """创建调酒记录模式"""
    pass


class CocktailRecordUpdate(BaseSchema):
    """更新调酒记录模式"""
    tag_id: Optional[int] = Field(None, description="标签ID")
    actual_ingredients: Optional[Dict[str, Any]] = Field(None, description="实际使用的成分和分量")
    taste_rating: Optional[TasteRating] = Field(None, description="口味评价")
    personal_rating: Optional[int] = Field(None, ge=1, le=5, description="个人评分（1-5）")
    notes: Optional[str] = Field(None, description="备注")


class CocktailRecordInDB(CocktailRecordBase, TimestampSchema):
    """数据库中的调酒记录模式"""
    id: int
    made_at: datetime


class CocktailRecord(CocktailRecordInDB):
    """调酒记录响应模式"""
    pass


class CocktailRecordWithRecipe(CocktailRecord):
    """包含配方信息的调酒记录"""
    recipe_name: str = Field(..., description="配方名称")
    recipe_description: Optional[str] = Field(None, description="配方描述")