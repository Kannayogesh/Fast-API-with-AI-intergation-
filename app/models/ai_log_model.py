from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.utils.db import Base

class AILog(Base):
    __tablename__ = "ai_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    prompt = Column(String)
    response = Column(String)
    tokens_used = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)