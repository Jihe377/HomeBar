from sqlalchemy import Column, Integer, String, Float, Text, Enum, Boolean
from sqlalchemy.orm import relationship

from app.db.base import Base
import enum


class ItemCategory(str, enum.Enum):
    """酒柜物品分类"""
    SPIRIT = "spirit"  # 基酒
    LIQUEUR = "liqueur"  # 利口酒
    WINE = "wine"  # 葡萄酒
    BEER = "beer"  # 啤酒
    MIXER = "mixer"  # 调酒饮料
    FRUIT = "fruit"  # 水果
    HERB = "herb"  # 香草
    OTHER = "other"  # 其他


class BarItem(Base):
    """酒柜物品模型"""
    __tablename__ = "bar_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    category = Column(Enum(ItemCategory), default=ItemCategory.OTHER)
    brand = Column(String(100))
    volume = Column(Float)  # 容量（毫升）
    current_volume = Column(Float)  # 当前剩余容量（毫升）
    abv = Column(Float)  # 酒精度（百分比）
    description = Column(Text)
    is_available = Column(Boolean, default=True)  # 是否可用
    
    # 关系
    recipe_ingredients = relationship("RecipeIngredient", back_populates="bar_item")
    shopping_items = relationship("ShoppingItem", back_populates="bar_item")
    
    def __repr__(self):
        return f"<BarItem {self.name} ({self.brand})>"