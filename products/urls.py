from django.urls import path, include

from views import Product

urlpatterns = [
    path('', views.all_products, name='products'),
]