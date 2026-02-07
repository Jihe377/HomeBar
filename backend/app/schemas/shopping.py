from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import datetime

from app.schemas.base import BaseSchema, TimestampSchema


class ShoppingStatus(str, Enum):
    """购物状态"""
    PENDING = "pending"
    PURCHASED = "purchased"
    CANCELLED = "cancelled"


class ShoppingItemBase(BaseSchema):
    """购物清单项目基础模式"""
    bar_item_id: Optional[int] = Field(None, description="酒柜物品ID")
    name: str = Field(..., min_length=1, max_length=100, description="物品名称")
    quantity: float = Field(..., ge=0, description="数量")
    unit: str = Field(..., min_length=1, max_length=20, description="单位")
    status: ShoppingStatus = Field(default=ShoppingStatus.PENDING, description="状态")
    priority: int = Field(default=1, ge=1, le=5, description="优先级（1-5，1最高）")
    notes: Optional[str] = Field(None, max_length=200, description="备注")


class ShoppingItemCreate(ShoppingItemBase):
    """创建购物清单项目模式"""
    pass


class ShoppingItemUpdate(BaseSchema):
    """更新购物清单项目模式"""
    bar_item_id: Optional[int] = Field(None, description="酒柜物品ID")
    name: Optional[str] = Field(None, min_length=1, max_length=100, description="物品名称")
    quantity: Optional[float] = Field(None, ge=0, description="数量")
    unit: Optional[str] = Field(None, min_length=1, max_length=20, description="单位")
    status: Optional[ShoppingStatus] = Field(None, description="状态")
    priority: Optional[int] = Field(None, ge=1, le=5, description="优先级（1-5，1最高）")
    notes: Optional[str] = Field(None, max_length=200, description="备注")


class ShoppingItemInDB(ShoppingItemBase, TimestampSchema):
    """数据库中的购物清单项目模式"""
    id: int


class ShoppingItem(ShoppingItemInDB):
    """购物清单项目响应模式"""
    pass