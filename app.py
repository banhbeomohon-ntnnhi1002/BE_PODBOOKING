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
