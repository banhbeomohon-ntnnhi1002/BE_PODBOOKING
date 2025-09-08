# payment_service.py

import stripe


PREMADE_PAYMENT_LINKS = {
    # Dán link của bạn vào đây
    "standard_booking": "https://buy.stripe.com/test_3cIbJ1cfVeh77mvbr56Zy01",
}


class PaymentService:
    def __init__(self):
        stripe.api_key = "pk_test_51S15N6FOoC1D1kORG4nhq9VR7LScuOeaTkLtiVO53Eu8wOXVValCYcFeJvSzWkVFwJRI4RyXGIAJRVsKn0fppPTz00D1bE1hBU"
        # ...

    def get_premade_stripe_link(self, product_key: str, booking_id: str) -> str | None:

        base_url = PREMADE_PAYMENT_LINKS.get(product_key)

        if not base_url:
            print(
                f"Lỗi: Không tìm thấy Payment Link cho sản phẩm '{product_key}'")
            return None

        final_url = f"{base_url}?client_reference_id={booking_id}"

        return final_url
