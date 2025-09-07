from sqlalchemy import Column, Integer, String, DateTime, Boolean
from infrastructure.databases.base import Base
from datetime import datetime

class Notification(Base):
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    message = Column(String(255), nullable=False)
    scheduled_time = Column(DateTime, nullable=True)  # Thêm thời gian hẹn
    is_read = Column(Boolean, default=False)          # Thay status -> is_read

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "message": self.message,
            "scheduled_time": self.scheduled_time.isoformat() if self.scheduled_time else None,
            "is_read": self.is_read
        }