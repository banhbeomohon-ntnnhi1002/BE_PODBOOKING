from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from api.auth.controller import auth_bp

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Tải cấu hình từ file config.py
app.config.from_object(Config)

# Khởi tạo JWTManager để hỗ trợ JWT
jwt = JWTManager(app)

# Đăng ký Blueprint của Auth
app.register_blueprint(auth_bp, url_prefix='/api/auth')

@app.route('/')
def home():
    return "Welcome to the Auth API!"

if __name__ == '__main__':
    # Chạy ứng dụng trên cổng 5000
    app.run(debug=True, port=5000)