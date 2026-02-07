from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.schemas.recipe import Tag, TagCreate
from app.services import tag_service

router = APIRouter()


@router.get("/", response_model=List[Tag])
def read_tags(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    """
    获取标签列表。
    """
    # tags = tag_service.get_tags(db, skip=skip, limit=limit)
    # return tags
    return []  # 占位符


@router.get("/{tag_id}", response_model=Tag)
def read_tag(tag_id: int, db: Session = Depends(get_db)):
    """
    根据ID获取标签。
    """
    # tag = tag_service.get_tag(db, tag_id=tag_id)
    # if tag is None:
    #     raise HTTPException(status_code=404, detail="标签未找到")
    # return tag
    raise HTTPException(status_code=404, detail="功能尚未实现")


@router.post("/", response_model=Tag)
def create_tag(tag: TagCreate, db: Session = Depends(get_db)):
    """
    创建标签。
    """
    # return tag_service.create_tag(db=db, tag=tag)
    raise HTTPException(status_code=501, detail="功能尚未实现")


@router.delete("/{tag_id}")
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    """
    删除标签。
    """
    # db_tag = tag_service.get_tag(db, tag_id=tag_id)
    # if db_tag is None:
    #     raise HTTPException(status_code=404, detail="标签未找到")
    # tag_service.delete_tag(db=db, tag_id=tag_id)
    # return {"message": "标签已删除"}
    raise HTTPException(status_code=501, detail="功能尚未实现")