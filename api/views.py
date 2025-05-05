# api/views.py
import json
import stripe
import requests

from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer
from .forms import ProductForm

# Stripe configuration
stripe.api_key = settings.STRIPE_SECRET_KEY

def home(request):
    return HttpResponse("Feel Food API ishlayapti 🚀")


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """Faqat o‘qish uchun API (GET)"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.order_by('-created_at')
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()

        # Telegram xabari
        text = (
            f"🛒 *YANGI BUYURTMA*\n"
            f"👤 Ism: {order.name}\n"
            f"📞 Tel: {order.phone}\n"
            f"📍 Manzil: {order.address}\n\n*Taomlar:*\n"
        ) + ''.join([f"• {i['name']} x{i['quantity']}\n" for i in order.items]) + (
            f"\n💲 Subtotal: ${order.subtotal}\n"
            f"🚚 Delivery: ${order.delivery_fee}\n"
            f"*Total:* ${order.total}"
        )

        resp = requests.post(
            f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage",
            json={'chat_id': settings.CHAT_ID, 'text': text, 'parse_mode': 'Markdown'}
        )
        if resp.status_code != 200:
            print(f"Telegram xatolik: {resp.text}")

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@api_view(['POST'])
@permission_classes([AllowAny])
def create_payment_intent(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    amount = data.get('amount')
    if amount is None:
        return JsonResponse({'error': 'Amount is required'}, status=400)
    if not isinstance(amount, int) or amount < 50:
        return JsonResponse({'error': 'Minimal miqdor $0.50 bo‘lishi kerak'}, status=400)

    try:
        intent = stripe.PaymentIntent.create(amount=amount, currency='usd')
        return JsonResponse({'clientSecret': intent.client_secret})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@api_view(['POST'])
@permission_classes([AllowAny])
def send_telegram(request):
    name    = request.data.get('name')
    phone   = request.data.get('phone')
    address = request.data.get('address')
    items   = request.data.get('items')

    if not all([name, phone, address, items]):
        return Response({'error': 'Missing fields'}, status=400)

    text = (
        f"🛒 *YANGI BUYURTMA*\n"
        f"👤 Ism: {name}\n"
        f"📞 Tel: {phone}\n"
        f"📍 Manzil: {address}\n\n*Taomlar:*\n"
    ) + ''.join([f"• {i['name']} x{i['quantity']}\n" for i in items])

    resp = requests.post(
        f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage",
        json={'chat_id': settings.CHAT_ID, 'text': text, 'parse_mode': 'Markdown'}
    )
    if resp.status_code != 200:
        return Response({'error': resp.text}, status=500)
    return Response({'success': 'Sent successfully'})
