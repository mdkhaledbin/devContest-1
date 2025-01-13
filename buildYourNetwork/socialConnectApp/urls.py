from django.urls import path
from .models import User
from .views import UserRegisterView, UserListView, UserDetailView, loginView
from .views import logoutView, FollowView, FollowersListView, FollowingListView
from .views import UnfollowView, BlockView, UnblockView, BlockedUsersListView, PostView
from .views import PostFeedView, RefreshTokensView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('users-list/', UserListView.as_view(), name = 'users-list'),
    path('users-list/<int:user_id>/', UserDetailView.as_view(), name = 'users-detail'),
    path('login/', loginView.as_view(), name = 'login'),
    path('logout/', logoutView.as_view(), name = 'logout'),
    # for following and unfollowing
    path('follow/<int:user_id>/', FollowView.as_view(), name='follow'),
    path('unfollow/<int:user_id>/', UnfollowView.as_view(), name='unfollow'),
    path('followers/<int:user_id>/', FollowersListView.as_view(), name='followers'),
    path('following/<int:user_id>/', FollowingListView.as_view(), name='following'),
    # for block and unblock
    path('block/<int:user_id>/', BlockView.as_view(), name='block'),
    path('unblock/<int:user_id>/', UnblockView.as_view(), name='unblock'),
    path('blocked-users', BlockedUsersListView.as_view(), name='blocked-users'),
    # for post
    path('post/', PostView.as_view(), name='post'),
    path('feed/', PostFeedView.as_view(), name='feed'),
    # for refresh token
    path('refresh-tokens/', RefreshTokensView.as_view(), name='refresh-tokens'),
]
