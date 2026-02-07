from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.schemas.cocktail_record import CocktailRecord, CocktailRecordCreate, CocktailRecordUpdate
from app.services import cocktail_record_service

router = APIRouter()


@router.get("/", response_model=List[CocktailRecord])
def read_cocktail_records(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    """
    获取调酒记录列表。
    """
    # records = cocktail_record_service.get_cocktail_records(db, skip=skip, limit=limit)
    # return records
    return []  # 占位符


@router.get("/{record_id}", response_model=CocktailRecord)
def read_cocktail_record(record_id: int, db: Session = Depends(get_db)):
    """
    根据ID获取调酒记录。
    """
    # record = cocktail_record_service.get_cocktail_record(db, record_id=record_id)
    # if record is None:
    #     raise HTTPException(status_code=404, detail="调酒记录未找到")
    # return record
    raise HTTPException(status_code=404, detail="功能尚未实现")


@router.post("/", response_model=CocktailRecord)
def create_cocktail_record(record: CocktailRecordCreate, db: Session = Depends(get_db)):
    """
    创建调酒记录。
    """
    # return cocktail_record_service.create_cocktail_record(db=db, record=record)
    raise HTTPException(status_code=501, detail="功能尚未实现")


@router.put("/{record_id}", response_model=CocktailRecord)
def update_cocktail_record(record_id: int, record: CocktailRecordUpdate, db: Session = Depends(get_db)):
    """
    更新调酒记录。
    """
    # db_record = cocktail_record_service.get_cocktail_record(db, record_id=record_id)
    # if db_record is None:
    #     raise HTTPException(status_code=404, detail="调酒记录未找到")
    # return cocktail_record_service.update_cocktail_record(db=db, db_record=db_record, record=record)
    raise HTTPException(status_code=501, detail="功能尚未实现")


@router.delete("/{record_id}")
def delete_cocktail_record(record_id: int, db: Session = Depends(get_db)):
    """
    删除调酒记录。
    """
    # db_record = cocktail_record_service.get_cocktail_record(db, record_id=record_id)
    # if db_record is None:
    #     raise HTTPException(status_code=404, detail="调酒记录未找到")
    # cocktail_record_service.delete_cocktail_record(db=db, record_id=record_id)
    # return {"message": "调酒记录已删除"}
    raise HTTPException(status_code=501, detail="功能尚未实现")