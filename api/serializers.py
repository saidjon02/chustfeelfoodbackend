from rest_framework import serializers
from .models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'img_url']

    def get_img_url(self, obj):
        request = self.context.get('request')
        image = obj.get_image()
        if image and request and image.startswith('/'):
            return request.build_absolute_uri(image)
        return image

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
