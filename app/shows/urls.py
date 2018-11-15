from django.urls import path

from . import views

app_name = 'shows'

urlpatterns = [
    path('show_list/', views.show_list, name='show-list'),
    path('show_detail/<int:pk>/', views.show_detail, name='show-detail'),
    path('show_rating/<int:rating_score>/', views.show_rating, name='show_rating'),
]