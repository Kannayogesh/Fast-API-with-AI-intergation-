from fastapi import APIRouter, Depends
from app.services.ai_service import summarize_task
from app.utils.role_checker import require_role

router = APIRouter()

@router.post("/summarize")
def summarize(data: dict, user=Depends(require_role("User"))):
    result = summarize_task(data["task_description"])
    return {
        "status": "success",
        "data": result
    }