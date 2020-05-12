from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('words/', views.words, name='index'),
]