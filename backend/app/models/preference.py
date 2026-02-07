from sqlalchemy import Column, Integer, String, Float, Boolean, Enum, Text
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import DateTime

from app.db.base import Base
import enum


class FlavorProfile(str, enum.Enum):
    """口味偏好"""
    SWEET = "sweet"  # 甜
    SOUR = "sour"  # 酸
    BITTER = "bitter"  # 苦
    FRUITY = "fruity"  # 果味
    HERBAL = "herbal"  # 草本
    SPICY = "spicy"  # 辛辣
    SMOKY = "smoky"  # 烟熏
    REFRESHING = "refreshing"  # 清爽
    STRONG = "strong"  # 烈


class TastePreference(Base):
    """口味偏好模型（简化版，假设每个设备/会话一个偏好）"""
    __tablename__ = "taste_preferences"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(100), unique=True, index=True)  # 会话ID或设备ID
    
    # 口味偏好（多选，用逗号分隔存储）
    preferred_flavors = Column(Text)  # 例如 "sweet,fruity,refreshing"
    
    # 强度偏好
    preferred_strength = Column(Float, default=0.5)  # 0.0-1.0，0.5为中等
    
    # 甜度偏好
    preferred_sweetness = Column(Float, default=0.5)  # 0.0-1.0
    
    # 酸度偏好
    preferred_sourness = Column(Float, default=0.5)  # 0.0-1.0
    
    # 其他设置
    exclude_ingredients = Column(Text)  # 排除的成分（逗号分隔）
    
    # 时间戳
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<TastePreference session={self.session_id}>"