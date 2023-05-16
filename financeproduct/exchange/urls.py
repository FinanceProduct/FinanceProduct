from django.urls import path
from . import views

app_name = 'exchange'
urlpatterns = [
    path('', views.exchange, name='exchange'),
    path('calculate/', views.calculate_exchange_rate, name='calculate'),
]
