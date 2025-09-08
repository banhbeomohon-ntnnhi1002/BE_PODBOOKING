from flask import Flask, jsonify
<<<<<<< HEAD
from src.api.swagger import spec
from src.api.controllers.todo_controller import bp as todo_bp
from src.api.controllers.analytics_controller import bp as analytics_bp
from src.api.middleware import middleware
from src.api.responses import success_response
from src.infrastructure.databases import init_db
from src.config import Config
from flasgger import Swagger
from src.config import SwaggerConfig
=======
from api.swagger import spec
from api.controllers.todo_controller import bp as todo_bp
from api.middleware import middleware
from api.responses import success_response
from infrastructure.databases import init_db
from config import Config
from flasgger import Swagger
from config import SwaggerConfig
>>>>>>> Services_Add-ons
from flask_swagger_ui import get_swaggerui_blueprint


def create_app():
    app = Flask(__name__)
    Swagger(app)
    # Đăng ký blueprint trước
    app.register_blueprint(todo_bp)
<<<<<<< HEAD
    app.register_blueprint(analytics_bp)
=======
>>>>>>> Services_Add-ons

     # Thêm Swagger UI blueprint
    SWAGGER_URL = '/docs'
    API_URL = '/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': "Todo API"}
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

<<<<<<< HEAD
    init_db(app)
=======
    try:
        init_db(app)
    except Exception as e:
        print(f"Error initializing database: {e}")
>>>>>>> Services_Add-ons

    # Register middleware
    middleware(app)

    # Register routes
<<<<<<< HEAD
    # Example: app.add_url_rule('/example', view_func=example_view)
    # Tự động quét tất cả các route đã đăng ký
    with app.test_request_context():
        for rule in app.url_map.iter_rules():
            if rule.endpoint.startswith('todo.'):
=======
    with app.test_request_context():
        for rule in app.url_map.iter_rules():
            # Thêm các endpoint khác nếu cần
            if rule.endpoint.startswith(('todo.', 'course.', 'user.')):
>>>>>>> Services_Add-ons
                view_func = app.view_functions[rule.endpoint]
                print(f"Adding path: {rule.rule} -> {view_func}")
                spec.path(view=view_func)

    @app.route("/swagger.json")
    def swagger_json():
        return jsonify(spec.to_dict())

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=6868, debug=True)