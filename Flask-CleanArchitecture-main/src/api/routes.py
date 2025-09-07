from src.api.controllers.todo_controller import bp as todo_bp
from src.api.controllers.feedback_controller import bp as feedback_bp
from src.api.controllers.notification_controller import bp as notification_bp

def register_routes(app):
    app.register_blueprint(todo_bp)
    app.register_blueprint(feedback_bp)
    app.register_blueprint(notification_bp)