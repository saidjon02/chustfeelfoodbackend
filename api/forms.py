from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # Modelda description yo‘qligi uchun faqat mavjud maydonlarni qo‘shamiz:
        fields = ['name', 'price', 'img']
