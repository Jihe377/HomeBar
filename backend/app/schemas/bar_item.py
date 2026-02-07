from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

from app.schemas.base import BaseSchema, TimestampSchema


class ItemCategory(str, Enum):
    """酒柜物品分类"""
    SPIRIT = "spirit"
    LIQUEUR = "liqueur"
    WINE = "wine"
    BEER = "beer"
    MIXER = "mixer"
    FRUIT = "fruit"
    HERB = "herb"
    OTHER = "other"


class BarItemBase(BaseSchema):
    """酒柜物品基础模式"""
    name: str = Field(..., min_length=1, max_length=100, description="物品名称")
    category: ItemCategory = Field(default=ItemCategory.OTHER, description="分类")
    brand: Optional[str] = Field(None, max_length=100, description="品牌")
    volume: Optional[float] = Field(None, ge=0, description="总容量（毫升）")
    current_volume: Optional[float] = Field(None, ge=0, description="当前剩余容量（毫升）")
    abv: Optional[float] = Field(None, ge=0, le=100, description="酒精度（百分比）")
    description: Optional[str] = Field(None, description="描述")
    is_available: bool = Field(default=True, description="是否可用")


class BarItemCreate(BarItemBase):
    """创建酒柜物品模式"""
    pass


class BarItemUpdate(BaseSchema):
    """更新酒柜物品模式"""
    name: Optional[str] = Field(None, min_length=1, max_length=100, description="物品名称")
    category: Optional[ItemCategory] = Field(None, description="分类")
    brand: Optional[str] = Field(None, max_length=100, description="品牌")
    volume: Optional[float] = Field(None, ge=0, description="总容量（毫升）")
    current_volume: Optional[float] = Field(None, ge=0, description="当前剩余容量（毫升）")
    abv: Optional[float] = Field(None, ge=0, le=100, description="酒精度（百分比）")
    description: Optional[str] = Field(None, description="描述")
    is_available: Optional[bool] = Field(None, description="是否可用")


class BarItemInDB(BarItemBase, TimestampSchema):
    """数据库中的酒柜物品模式"""
    id: int


class BarItem(BarItemInDB):
    """酒柜物品响应模式"""
    pass