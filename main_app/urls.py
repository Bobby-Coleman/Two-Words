from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('words/', views.words, name='index'),
    path('words/list', views.words_list, name='list'),
    path('accounts/signup/', views.signup, name='signup'),
]