from flask import Flask
from src.config import Config
from .api.middleware import middleware
from .api.routes import register_routes
from .infrastructure.databases import init_db
from .app_logging import setup_logging
from src.api.analytics.analytics_router import analytics_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    setup_logging()
    init_db(app)
    middleware(app)
    register_routes(app)
    app.register_blueprint(analytics_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
