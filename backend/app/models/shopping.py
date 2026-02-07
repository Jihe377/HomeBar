from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import DateTime

from app.db.base import Base
import enum


class ShoppingStatus(str, enum.Enum):
    """购物状态"""
    PENDING = "pending"
    PURCHASED = "purchased"
    CANCELLED = "cancelled"


class ShoppingItem(Base):
    """购物清单项目模型"""
    __tablename__ = "shopping_items"

    id = Column(Integer, primary_key=True, index=True)
    bar_item_id = Column(Integer, ForeignKey("bar_items.id"))
    name = Column(String(100), nullable=False)  # 物品名称（如果bar_item_id为空则使用此字段）
    quantity = Column(Float, nullable=False)  # 数量
    unit = Column(String(20), nullable=False)  # 单位
    status = Column(Enum(ShoppingStatus), default=ShoppingStatus.PENDING)
    priority = Column(Integer, default=1)  # 优先级（1-5，1最高）
    notes = Column(String(200))  # 备注
    
    # 时间戳
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # 关系
    bar_item = relationship("BarItem", back_populates="shopping_items")
    
    def __repr__(self):
        return f"<ShoppingItem {self.name} ({self.status})>"