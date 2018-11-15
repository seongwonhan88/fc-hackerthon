from django.urls import path

from . import views

app_name = 'members'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('user_pick/<int:pk>', views.user_pick, name='user-pick'),
]