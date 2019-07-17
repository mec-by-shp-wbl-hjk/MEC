from django.contrib import admin
from MECboard.models import Board, Comment

class BoardAdmin(admin.ModelAdmin):
    list_display = ("writer", "title", "content")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("writer", "content")

admin.site.register(Board, BoardAdmin)
admin.site.register(Comment, CommentAdmin)