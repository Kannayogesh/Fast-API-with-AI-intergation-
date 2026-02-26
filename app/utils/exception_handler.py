from fastapi.responses import JSONResponse
from fastapi import Request

async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=400,
        content={
            "status": "error",
            "message": str(exc),
            "code": 400
        }
    )