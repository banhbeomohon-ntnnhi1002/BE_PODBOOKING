from infrastructure.databases.base import Base
from infrastructure.databases.mssql import engine
from infrastructure.models.feedback_model import Feedback
from infrastructure.models.notification_model import Notification

if __name__ == "__main__":
    print("Đang tạo database và các bảng...")
    Base.metadata.create_all(bind=engine)
    print("Tạo database thành công!")