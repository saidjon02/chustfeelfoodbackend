# api/serializers.py

from rest_framework import serializers
from .models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    get_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'get_image']

    def get_get_image(self, obj):
        request = self.context.get('request')
        image = obj.get_image()
        if image and request and image.startswith('/'):
            return request.build_absolute_uri(image)
        return image

class ItemSerializer(serializers.Serializer):
    name = serializers.CharField()
    quantity = serializers.IntegerField()

class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'name', 'phone', 'address', 'items', 'subtotal', 'delivery_fee', 'total', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(items=items_data, **validated_data)
        return order
