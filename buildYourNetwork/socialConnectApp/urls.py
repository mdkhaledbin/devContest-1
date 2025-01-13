from django.urls import path
from .models import User
from .views import UserRegisterView, UserListView, UserDetailView, loginView, logoutView, FollowView, FollowersListView, FollowingListView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('users-list/', UserListView.as_view(), name = 'users-list'),
    path('users-list/<int:user_id>/', UserDetailView.as_view(), name = 'users-detail'),
    path('login/', loginView.as_view(), name = 'login'),
    path('logout/', logoutView.as_view(), name = 'logout'),
    # for following and unfollowing
    path('follow/<int:user_id>/', FollowView.as_view(), name='follow'),
    # path('unfollow/<int:user_id>/', UnfollowView.as_view(), name='unfollow'),
    path('followers/<int:user_id>/', FollowersListView.as_view(), name='followers'),
    path('following/<int:user_id>/', FollowingListView.as_view(), name='following'),
]
