from infrastructure.databases.session import db_session
from domain.models.notification_model import Notification

class NotificationRepository:
    def save(self, notification):
        db_session.add(notification)
        db_session.commit()
        return notification

    def get_all(self):
        return db_session.query(Notification).all()

    def mark_as_read(self, notification_id):
        notification = db_session.query(Notification).filter_by(id=notification_id).first()
        if notification:
            notification.is_read = True
            db_session.commit()
            return notification
        return None

    def delete(self, notification_id):
        notification = db_session.query(Notification).filter_by(id=notification_id).first()
        if notification:
            db_session.delete(notification)
            db_session.commit()
            return True
        return False