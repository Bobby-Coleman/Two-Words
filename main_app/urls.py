from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('words/', views.words, name='index'),
    path('words/list', views.words_list, name='list'),
    path('accounts/signup/', views.signup, name='signup'),
    path('words/<int:word_id>/', views.words_detail, name='detail'),
    path('words/<int:word_id>/add_comment', views.add_comment, name='add_comment'),
    path('words/<int:word_id>/<int:comment_id>/update/', views.comment_view, name='comment_view'),
    # path('words/<int:word_id>/', views.comment_update, name='comment_update'),
]