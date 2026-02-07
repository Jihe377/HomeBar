from sqlalchemy import Column, Integer, String, Text, Float, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import DateTime

from app.db.base import Base
import enum


class TasteRating(str, enum.Enum):
    """口味评价"""
    TOO_SWEET = "too_sweet"  # 太甜
    TOO_SOUR = "too_sour"  # 太酸
    TOO_BITTER = "too_bitter"  # 太苦
    TOO_STRONG = "too_strong"  # 太烈
    TOO_WEAK = "too_weak"  # 太淡
    PERFECT = "perfect"  # 完美
    GOOD = "good"  # 好
    OK = "ok"  # 一般
    BAD = "bad"  # 差


class CocktailRecord(Base):
    """调酒记录模型"""
    __tablename__ = "cocktail_records"

    id = Column(Integer, primary_key=True, index=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"), nullable=False)
    tag_id = Column(Integer, ForeignKey("tags.id"))
    
    # 实际使用的分量记录（JSON格式存储，存储成分ID和实际用量）
    # 这里简化为文本字段，实际可使用JSON字段
    actual_ingredients = Column(Text)
    
    # 评价
    taste_rating = Column(Enum(TasteRating))
    personal_rating = Column(Integer)  # 个人评分（1-5）
    notes = Column(Text)  # 备注
    
    # 时间戳
    made_at = Column(DateTime(timezone=True), server_default=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # 关系
    recipe = relationship("Recipe", back_populates="cocktail_records")
    tag = relationship("Tag", back_populates="cocktail_records")
    
    def __repr__(self):
        return f"<CocktailRecord {self.recipe.name} @ {self.made_at}>"