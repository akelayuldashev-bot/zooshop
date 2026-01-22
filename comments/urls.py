from django.urls import path
from .views import add_comment, delete_comment

app_name = 'comments'

urlpatterns = [
    path('add/<int:product_id>/', add_comment, name='add_comment'),
    path('delete/<int:comment_id>/', delete_comment, name='delete_comment'),
]
