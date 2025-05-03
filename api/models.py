from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='products/', null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)

    def get_image(self):
        if self.img:
            return self.img.url
        elif self.image_url:
            return self.image_url
        return None

    def __str__(self):
        return self.name

# models.py

class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    items = models.JSONField()  # MUHIM: frontenddan kelgan cartItems shu yerga tushadi
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Order #{self.id} by {self.name}"
