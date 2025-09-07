from infrastructure.repositories.notification_repository import NotificationRepository
from domain.models.notification_model import Notification
from datetime import datetime

class NotificationService:
    def __init__(self):
        self.repo = NotificationRepository()

    def get_all_notifications(self):
        return self.repo.get_all()

    def create_notification(self, user_id, message, scheduled_time=None):
        # Kiểm tra dữ liệu bắt buộc
        if not user_id:
            raise ValueError("user_id là bắt buộc")
        if not message or message.strip() == "":
            raise ValueError("message không được để trống")

        # Xử lý thời gian nếu có
        scheduled_dt = None
        if scheduled_time:
            try:
                scheduled_dt = datetime.fromisoformat(scheduled_time)
            except ValueError:
                raise ValueError("scheduled_time phải đúng định dạng ISO (YYYY-MM-DDTHH:MM:SS)")
        
        # Tạo đối tượng Notification
        notification = Notification(user_id=user_id, message=message.strip(), scheduled_time=scheduled_dt, is_read=False)
        
        # Lưu vào DB
        return self.repo.save(notification)

    def mark_as_read(self, notif_id):
        if not notif_id:
            raise ValueError("notif_id là bắt buộc")
        
        return self.repo.mark_as_read(notif_id)