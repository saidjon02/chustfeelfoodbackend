from django.contrib import admin
from django.urls import path, include
from api.views import home  # bu opsional, agar "API ishlayapti" deb tekshirmoqchi bo‘lsang

urlpatterns = [
    path('', home, name='home'),  # optional: API is alive
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
