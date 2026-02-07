from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum
from datetime import datetime

from app.schemas.base import BaseSchema, TimestampSchema


class FlavorProfile(str, Enum):
    """口味偏好"""
    SWEET = "sweet"
    SOUR = "sour"
    BITTER = "bitter"
    FRUITY = "fruity"
    HERBAL = "herbal"
    SPICY = "spicy"
    SMOKY = "smoky"
    REFRESHING = "refreshing"
    STRONG = "strong"


class TastePreferenceBase(BaseSchema):
    """口味偏好基础模式"""
    session_id: str = Field(..., min_length=1, max_length=100, description="会话ID或设备ID")
    
    # 口味偏好
    preferred_flavors: Optional[List[FlavorProfile]] = Field(None, description="偏好口味列表")
    
    # 强度偏好
    preferred_strength: float = Field(default=0.5, ge=0, le=1, description="强度偏好（0.0-1.0）")
    
    # 甜度偏好
    preferred_sweetness: float = Field(default=0.5, ge=0, le=1, description="甜度偏好（0.0-1.0）")
    
    # 酸度偏好
    preferred_sourness: float = Field(default=0.5, ge=0, le=1, description="酸度偏好（0.0-1.0）")
    
    # 其他设置
    exclude_ingredients: Optional[List[str]] = Field(None, description="排除的成分列表")


class TastePreferenceCreate(TastePreferenceBase):
    """创建口味偏好模式"""
    pass


class TastePreferenceUpdate(BaseSchema):
    """更新口味偏好模式"""
    preferred_flavors: Optional[List[FlavorProfile]] = Field(None, description="偏好口味列表")
    preferred_strength: Optional[float] = Field(None, ge=0, le=1, description="强度偏好（0.0-1.0）")
    preferred_sweetness: Optional[float] = Field(None, ge=0, le=1, description="甜度偏好（0.0-1.0）")
    preferred_sourness: Optional[float] = Field(None, ge=0, le=1, description="酸度偏好（0.0-1.0）")
    exclude_ingredients: Optional[List[str]] = Field(None, description="排除的成分列表")


class TastePreferenceInDB(TastePreferenceBase, TimestampSchema):
    """数据库中的口味偏好模式"""
    id: int


class TastePreference(TastePreferenceInDB):
    """口味偏好响应模式"""
    pass