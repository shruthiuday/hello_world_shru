from django.urls import path
from . import views

urlpatterns = [
    path('hw1/', views.hw1, name='hw1'),
]