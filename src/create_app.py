from flask import Flask
<<<<<<< HEAD
from src.config import Config
from .api.middleware import middleware
from .api.routes import register_routes
from .infrastructure.databases import init_db
from .app_logging import setup_logging
from src.api.analytics.analytics_router import analytics_bp
=======
from .config import Config
from .api.middleware import setup_middleware
from .api.routes import register_routes
from .infrastructure.databases import init_db
from .app_logging import setup_logging
>>>>>>> Services_Add-ons

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

<<<<<<< HEAD
    setup_logging()
    init_db(app)
    middleware(app)
    register_routes(app)
    app.register_blueprint(analytics_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
=======
    setup_logging(app)
    init_db(app)
    setup_middleware(app)
    register_routes(app)

    return app
>>>>>>> Services_Add-ons
