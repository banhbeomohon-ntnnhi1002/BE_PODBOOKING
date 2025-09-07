from infrastructure.repositories.feedback_repository import FeedbackRepository
from domain.models.feedback_model import Feedback

class FeedbackService:
    def __init__(self):
        self.repo = FeedbackRepository()

    def get_all_feedbacks(self):
        return self.repo.get_all()

    def create_feedback(self, user_id, message, rating):
        # Kiểm tra dữ liệu bắt buộc
        if not user_id:
            raise ValueError("user_id là bắt buộc")
        if not message or message.strip() == "":
            raise ValueError("message không được để trống")
        if rating is None:
            raise ValueError("rating là bắt buộc")
        
        # Kiểm tra kiểu dữ liệu
        try:
            rating = int(rating)
        except ValueError:
            raise ValueError("rating phải là số nguyên")
        
        # Kiểm tra giá trị rating
        if rating < 1 or rating > 5:
            raise ValueError("rating phải từ 1 đến 5")

        # Tạo đối tượng Feedback
        feedback = Feedback(user_id=user_id, message=message.strip(), rating=rating)
        
        # Lưu vào DB
        return self.repo.save(feedback)