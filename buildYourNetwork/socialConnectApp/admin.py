from django.contrib import admin
from .models import Follower, Blocked, Post, Like
# Register your models here.
admin.site.register(Follower)
admin.site.register(Blocked)
admin.site.register(Post)
admin.site.register(Like)