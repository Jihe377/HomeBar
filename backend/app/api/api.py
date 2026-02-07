from fastapi import APIRouter

from app.api.endpoints import (
    bar_items,
    recipes,
    cocktail_records,
    shopping,
    preferences,
    tags,
    utils,
)

api_router = APIRouter()

# 包含各个模块的路由
api_router.include_router(bar_items.router, prefix="/bar-items", tags=["酒柜物品"])
api_router.include_router(recipes.router, prefix="/recipes", tags=["配方"])
api_router.include_router(cocktail_records.router, prefix="/cocktail-records", tags=["调酒记录"])
api_router.include_router(shopping.router, prefix="/shopping", tags=["购物清单"])
api_router.include_router(preferences.router, prefix="/preferences", tags=["口味偏好"])
api_router.include_router(tags.router, prefix="/tags", tags=["标签"])
api_router.include_router(utils.router, prefix="/utils", tags=["工具"])