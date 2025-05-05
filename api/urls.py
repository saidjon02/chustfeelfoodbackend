from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProductViewSet, OrderViewSet,
    create_payment_intent, send_telegram,
    product_create, product_detail, product_update, product_delete,
    product_list_api, product_create_api
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

    # Template-based CRUD views
    path('products/create/', product_create, name='product_create'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('products/<int:pk>/edit/', product_update, name='product_update'),
    path('products/<int:pk>/delete/', product_delete, name='product_delete'),

    # Optional: simple JSON API for frontend (like React)
    path('products/json/', product_list_api, name='product_list_api'),
    path('products/json/create/', product_create_api, name='product_create_api'),
]
