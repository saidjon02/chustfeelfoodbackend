# api/models.py
from django.db import models

# api/models.py

from django.db import models

class Product(models.Model):
    FOOD  = 'food'
    DRINK = 'drink'
    CAKE  = 'cake'
    CATEGORY_CHOICES = [
        (FOOD,  '🍔 Taomlar'),
        (DRINK, '🥤 Ichimliklar'),
        (CAKE,  '🍰 Desertlar'),
    ]

    name      = models.CharField(max_length=255)
    price     = models.DecimalField(max_digits=10, decimal_places=2)
    img       = models.ImageField(upload_to='products/', blank=True, null=True)
    image_url = models.URLField(null=True, blank=True)
    category  = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default=FOOD,
        help_text="Kategoriya: ovqatlar, ichimliklar yoki tortlar"
    )

    def get_image(self):
        if self.img and hasattr(self.img, 'url'):
            return str(self.img.url)
        elif self.image_url:
            return self.image_url
        return ''

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

class Order(models.Model):
    name         = models.CharField(max_length=255)
    phone        = models.CharField(max_length=50)
    address      = models.TextField()
    items        = models.JSONField()
    subtotal     = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2)
    total        = models.DecimalField(max_digits=10, decimal_places=2)
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.name}"
