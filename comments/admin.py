from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'create_at')
    list_filter = ('create_at', 'product')
    search_fields = ('user__username', 'product__title', 'text')