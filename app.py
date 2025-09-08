<<<<<<< HEAD
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
    app.run(debug=True, port=5000)
=======
# app.py

from flask import Flask, request, jsonify
from payment_service import PaymentService
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
payment_service = PaymentService()


@app.route('/get-stripe-link', methods=['POST'])
def get_stripe_link():
    data = request.get_json()
    product_key = data.get('product_key')
    booking_id = data.get('booking_id')

    if not all([product_key, booking_id]):
        return jsonify({'error': 'product_key và booking_id là bắt buộc'}), 400

    payment_link_url = payment_service.get_premade_stripe_link(
        product_key=product_key,
        booking_id=booking_id
    )

    if payment_link_url:
        return jsonify({'payment_link_url': payment_link_url})
    else:
        return jsonify({'error': 'Không tìm thấy link thanh toán cho sản phẩm này'}), 404


if __name__ == '__main__':
    app.run(debug=True, port=4242)
>>>>>>> payment
