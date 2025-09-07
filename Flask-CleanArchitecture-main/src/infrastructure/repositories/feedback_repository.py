from infrastructure.databases.session import db_session
from domain.models.feedback_model import Feedback

class FeedbackRepository:
    def save(self, feedback):
        db_session.add(feedback)
        db_session.commit()
        return feedback

    def get_all(self):
        return db_session.query(Feedback).all()

    def get_by_id(self, feedback_id):
        return db_session.query(Feedback).filter_by(id=feedback_id).first()

    def delete(self, feedback_id):
        feedback = self.get_by_id(feedback_id)
        if feedback:
            db_session.delete(feedback)
            db_session.commit()
            return True
        return False