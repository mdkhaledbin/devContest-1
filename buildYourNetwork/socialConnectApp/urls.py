from django.urls import path
from .models import User
from .views import UserRegisterView, UserListView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('users-list/', UserListView.as_view(), name = 'users-list'),
    
]
