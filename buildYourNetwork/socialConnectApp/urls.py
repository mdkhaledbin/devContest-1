from django.urls import path
from .models import User
from .views import UserRegisterView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name = 'register')
]
