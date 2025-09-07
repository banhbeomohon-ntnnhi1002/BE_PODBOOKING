from flask import Blueprint, request, jsonify
from services.feedback_service import FeedbackService

bp = Blueprint('feedback', __name__, url_prefix='/feedback')
service = FeedbackService()

@bp.route('/', methods=['GET'])
def get_feedbacks():
    feedbacks = service.get_all_feedbacks()
    return jsonify([{
        "id": f.id,
        "user_id": f.user_id,
        "message": f.message,
        "rating": f.rating
    } for f in feedbacks]), 200

@bp.route('/', methods=['POST'])
def add_feedback():
    data = request.get_json()
    try:
        feedback = service.create_feedback(
            user_id=data.get('user_id'),
            message=data.get('message'),
            rating=data.get('rating')
        )
        return jsonify({
            "id": feedback.id,
            "user_id": feedback.user_id,
            "message": feedback.message,
            "rating": feedback.rating
        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400