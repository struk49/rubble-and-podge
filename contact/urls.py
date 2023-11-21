from django.urls import path, include

app_name = 'contact'

from . import views

urlpatterns = [
    path('contact/', views.contact_us, name='contact_us'),
]