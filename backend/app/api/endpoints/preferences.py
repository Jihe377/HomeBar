from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.preference import TastePreference, TastePreferenceCreate, TastePreferenceUpdate
from app.services import preference_service

router = APIRouter()


@router.get("/{session_id}", response_model=TastePreference)
def read_preference(session_id: str, db: Session = Depends(get_db)):
    """
    获取口味偏好。
    """
    # preference = preference_service.get_preference(db, session_id=session_id)
    # if preference is None:
    #     raise HTTPException(status_code=404, detail="口味偏好未找到")
    # return preference
    raise HTTPException(status_code=404, detail="功能尚未实现")


@router.post("/", response_model=TastePreference)
def create_preference(preference: TastePreferenceCreate, db: Session = Depends(get_db)):
    """
    创建口味偏好。
    """
    # return preference_service.create_preference(db=db, preference=preference)
    raise HTTPException(status_code=501, detail="功能尚未实现")


@router.put("/{session_id}", response_model=TastePreference)
def update_preference(session_id: str, preference: TastePreferenceUpdate, db: Session = Depends(get_db)):
    """
    更新口味偏好。
    """
    # db_preference = preference_service.get_preference(db, session_id=session_id)
    # if db_preference is None:
    #     raise HTTPException(status_code=404, detail="口味偏好未找到")
    # return preference_service.update_preference(db=db, db_preference=db_preference, preference=preference)
    raise HTTPException(status_code=501, detail="功能尚未实现")


@router.delete("/{session_id}")
def delete_preference(session_id: str, db: Session = Depends(get_db)):
    """
    删除口味偏好。
    """
    # db_preference = preference_service.get_preference(db, session_id=session_id)
    # if db_preference is None:
    #     raise HTTPException(status_code=404, detail="口味偏好未找到")
    # preference_service.delete_preference(db=db, session_id=session_id)
    # return {"message": "口味偏好已删除"}
    raise HTTPException(status_code=501, detail="功能尚未实现")