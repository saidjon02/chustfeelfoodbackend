from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProductViewSet, OrderViewSet,
    create_payment_intent, send_telegram
)

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    # DRF router-based API
    path('', include(router.urls)),

    # Stripe & Telegram
    path('create-payment-intent/', create_payment_intent, name='create-payment-intent'),
    path('send-telegram/', send_telegram, name='send-telegram'),
]
