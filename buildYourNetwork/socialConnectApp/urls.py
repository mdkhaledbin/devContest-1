from django.urls import path
from .models import User
from .views import UserRegisterView, UserListView, UserDetailView, loginView, logoutView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('users-list/', UserListView.as_view(), name = 'users-list'),
    path('users-list/<int:user_id>/', UserDetailView.as_view(), name = 'users-detail'),
    path('login/', loginView.as_view(), name = 'login'),
    path('logout/', logoutView.as_view(), name = 'logout'),
]
