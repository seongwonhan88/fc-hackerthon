from django.urls import path

from . import views

app_name = 'shows'

urlpatterns = [
    path('show_list/', views.show_list, name='show-list'),
    path('show_detail/<int:show_pk>/', views.show_detail, name='show-detail'),
    path('show_rating/<int:rating_score>/', views.show_rating, name='show-rating'),
    path('<int:show_pk>/comment/create', views.comment_create, name='comment_create'),
    path('<int:show_pk>/pick_toggle/', views.show_pick_toggle, name='show_pick_toggle'),
]