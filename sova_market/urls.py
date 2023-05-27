from django.contrib import admin
from django.urls import path, include

# Импортируем созданные нами представления
from .views import ProductsList, ProductDetail

urlpatterns = [
   path('admin/', admin.site.urls),
   path('pages/', include('django.contrib.flatpages.urls')),  # < вот тут
]