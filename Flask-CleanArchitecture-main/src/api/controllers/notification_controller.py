from flask import Blueprint, request, jsonify
from services.notification_service import NotificationService

bp = Blueprint('notification', __name__, url_prefix='/notification')
service = NotificationService()

@bp.route('/', methods=['GET'])
def get_notifications():
    notifications = service.get_all_notifications()
    return jsonify([{
        "id": n.id,
        "user_id": n.user_id,
        "message": n.message,
        "scheduled_time": n.scheduled_time,
        "is_read": n.is_read
    } for n in notifications]), 200

@bp.route('/', methods=['POST'])
def add_notification():
    data = request.get_json()
    try:
        notification = service.create_notification(
            user_id=data.get('user_id'),
            message=data.get('message'),
            scheduled_time=data.get('scheduled_time')  # ISO format nếu có
        )
        return jsonify({
            "id": notification.id,
            "user_id": notification.user_id,
            "message": notification.message,
            "scheduled_time": str(notification.scheduled_time),
            "is_read": notification.is_read
        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@bp.route('/<int:notif_id>/read', methods=['PUT'])
def mark_notification_as_read(notif_id):
    notif = service.mark_as_read(notif_id)
    if notif:
        return jsonify({
            "id": notif.id,
            "user_id": notif.user_id,
            "message": notif.message,
            "is_read": notif.is_read
        }), 200
    return jsonify({"message": "Notification not found"}), 404