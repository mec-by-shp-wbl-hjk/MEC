from django.contrib import admin
from MECboard.models import Board, Comment
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile

class BoardAdmin(admin.ModelAdmin):
    list_display = ("writer", "title", "content")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("writer", "content", "vote")

admin.site.register(Board, BoardAdmin)
admin.site.register(Comment, CommentAdmin)

class ProfileInline(admin.StackedInline):
    model = Profile
    con_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)