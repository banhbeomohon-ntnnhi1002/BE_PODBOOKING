from sqlalchemy import Column, Integer, String, Text
from infrastructure.databases.base import Base

class Feedback(Base):
    __tablename__ = 'feedbacks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)  # Thay user -> user_id
    message = Column(Text, nullable=False)     # Thay comment -> message
    rating = Column(Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "message": self.message,
            "rating": self.rating
        }