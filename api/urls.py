from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet, create_payment_intent

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'orders',   OrderViewSet,   basename='order')

urlpatterns = [
    path('', include(router.urls)),
    path('create-payment-intent/', create_payment_intent, name='create-payment-intent'),
]
