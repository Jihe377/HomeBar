from sqlalchemy import Column, Integer, String, Text, Float, Boolean, Enum, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import DateTime

from app.db.base import Base
import enum


# 配方与标签的关联表（多对多）
recipe_tags = Table(
    "recipe_tags",
    Base.metadata,
    Column("recipe_id", Integer, ForeignKey("recipes.id")),
    Column("tag_id", Integer, ForeignKey("tags.id")),
)


class DifficultyLevel(str, enum.Enum):
    """配方难度级别"""
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class Recipe(Base):
    """配方模型"""
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False, index=True)
    description = Column(Text)
    instructions = Column(Text, nullable=False)  # 制作步骤
    glassware = Column(String(100))  # 所需杯具
    difficulty = Column(Enum(DifficultyLevel), default=DifficultyLevel.MEDIUM)
    is_public = Column(Boolean, default=True)  # 是否公开
    is_iba_official = Column(Boolean, default=False)  # 是否是IBA官方配方
    source = Column(String(200))  # 来源（如URL、书籍名）
    prep_time = Column(Integer)  # 准备时间（分钟）
    total_time = Column(Integer)  # 总时间（分钟）
    rating = Column(Float, default=0.0)  # 平均评分
    rating_count = Column(Integer, default=0)  # 评分次数
    
    # 时间戳
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # 关系
    ingredients = relationship("RecipeIngredient", back_populates="recipe", cascade="all, delete-orphan")
    tags = relationship("Tag", secondary=recipe_tags, back_populates="recipes")
    cocktail_records = relationship("CocktailRecord", back_populates="recipe")
    
    def __repr__(self):
        return f"<Recipe {self.name}>"


class RecipeIngredient(Base):
    """配方成分模型"""
    __tablename__ = "recipe_ingredients"

    id = Column(Integer, primary_key=True, index=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"), nullable=False)
    bar_item_id = Column(Integer, ForeignKey("bar_items.id"))
    name = Column(String(100), nullable=False)  # 成分名称（如果bar_item_id为空则使用此字段）
    quantity = Column(Float, nullable=False)  # 数量
    unit = Column(String(20), nullable=False)  # 单位（ml, oz, dash, piece等）
    note = Column(String(200))  # 备注（如"新鲜榨汁"）
    
    # 关系
    recipe = relationship("Recipe", back_populates="ingredients")
    bar_item = relationship("BarItem", back_populates="recipe_ingredients")
    
    def __repr__(self):
        return f"<RecipeIngredient {self.name} {self.quantity}{self.unit}>"


class Tag(Base):
    """标签模型（用于配方分类）"""
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, unique=True, index=True)
    color = Column(String(7))  # 颜色代码（如#FF0000）
    
    # 关系
    recipes = relationship("Recipe", secondary=recipe_tags, back_populates="tags")
    cocktail_records = relationship("CocktailRecord", back_populates="tag")
    
    def __repr__(self):
        return f"<Tag {self.name}>"