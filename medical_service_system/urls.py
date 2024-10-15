
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('medical_service/', include('medical_service.urls')),  # Đưa vào các URL từ ứng dụng medical_service
]
