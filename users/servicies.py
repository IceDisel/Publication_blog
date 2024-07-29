import stripe
from django.conf import settings
from smsaero import SmsAero

stripe.api_key = settings.STRIPE_API_KEY


def send_sms(phone: int, message: str):
    """
    Функция отправки SMS-сообщения
    """

    email = settings.SMSAERO_EMAIL
    if isinstance(email, tuple):
        email = email[0]
    key = settings.SMSAERO_API_KEY
    api = SmsAero(email, key)
    return api.send_sms(phone, message)


def create_session():
    """
    Функция оплаты с помощью сервиса Stripe
    """

    stripe_session = stripe.checkout.Session.create(
        line_items=[
            {
                "price_data": {
                    "currency": "rub",
                    "unit_amount": settings.PRODUCT_PRICE * 100,
                    "product_data": {
                        "name": "Премиум подписка",
                    },
                },
                "quantity": 1,
            },
        ],
        mode="payment",
        success_url='http://127.0.0.1:8000/payment_success',
        cancel_url='http://127.0.0.1:8000/payment_cancel'
    )
    return stripe_session.get('id'), stripe_session.get('url')
