from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .models import Comment
from shop.models import Product
from django.http import HttpResponseForbidden

@login_required
def add_comment(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.product = product
            comment.save()

    return redirect(request.META.get('HTTP_REFERER', 'shop:index'))

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.user != request.user:
        return HttpResponseForbidden('Вы не можете удалить чужой комментарий')

    if request.method == 'POST':
        comment.delete()

    return redirect(request.META.get('HTTP_REFERER', 'shop:index'))