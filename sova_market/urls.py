from django.urls import path, include

# Импортируем созданные нами представления
from .views import ProductsList, ProductDetail

urlpatterns = [
      path('', ProductsList.as_view()),
      path('<int:pk>', ProductDetail.as_view()),
]

# include('django.contrib.flatpages.urls')
# admin.site.urls