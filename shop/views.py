from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Favorite, Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import RegisterForm, ProfileAvatarForm
from django import forms
from django.contrib.auth.decorators import login_required
import stripe
from django.conf import settings
from django.urls import reverse
from django.http import JsonResponse


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    favorite_ids = []
    if request.user.is_authenticated:
        favorite_ids = Favorite.objects.filter(
            user=request.user
        ).values_list('product_id', flat=True)

    return render(request, 'shop/index.html', {
        'products': products,
        'categories': categories,
        'current_category': None,
        'favorite_ids': favorite_ids,
    })


def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()

    favorite_ids = []
    if request.user.is_authenticated:
        favorite_ids = Favorite.objects.filter(
            user=request.user
        ).values_list('product_id', flat=True)

    return render(request, 'shop/index.html', {
        'products': products,
        'categories': categories,
        'current_category': category,
        'favorite_ids': favorite_ids,
    })


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart

    return redirect('shop:cart')


def cart(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())

    cart_items = []
    total_price = 0

    for product in products:
        quantity = cart[str(product.id)]
        total = product.price * quantity
        total_price += total

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': total
        })

    return render(request, 'shop/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('shop:cart')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('shop:index')
    else:
        form = RegisterForm()

    return render(request, 'shop/register.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('shop:index')

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите имя пользователя'
        })
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        })
    )

#===================================================================

@login_required
def add_to_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Favorite.objects.get_or_create(
        user=request.user,
        product=product
    )
    return redirect(request.META.get('HTTP_REFERER', 'shop:index'))

@login_required
def remove_from_favorite(request, product_id):
    Favorite.objects.filter(
        user=request.user,
        product_id=product_id
    ).delete()
    return redirect('shop:favorites')

@login_required
def favorites(request):
    items = Favorite.objects.filter(user=request.user)
    return render(request, 'shop/favorite.html', {
        'items': items
    })

@login_required()
def checkout(request):
    cart = request.session.get('cart', {})

    if not cart:
        return redirect('shop:cart')

    products = Product.objects.filter(id__in=cart.keys())

    total_price = 0
    for product in products:
        total_price += product.price * cart[str(product.id)]

    return render(request, 'shop/checkout.html', {
        'products': products,
        'total_price': total_price
    })

@login_required()
def payment_success(request):
    request.session['cart'] = {}
    return render(request, 'shop/payment_success.html')

@login_required
def profile_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileAvatarForm(
            request.POST,
            request.FILES,
            instance=profile
        )
        if form.is_valid():
            form.save()
            return redirect('shop:profile')
    else:
        form = ProfileAvatarForm(instance=profile)

    return render(request, 'shop/profile.html', {
        'profile': profile,
        'form': form
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    categories = Category.objects.all()

    favorite_ids = []
    if request.user.is_authenticated:
        favorite_ids = Favorite.objects.filter(
            user=request.user
        ).values_list('product_id', flat=True)

    return render(request, 'shop/product_detail.html', {
        'product': product,
        'categories': categories,
        'favorite_ids': favorite_ids,
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    categories = Category.objects.all()

    favorite_ids = []
    if request.user.is_authenticated:
        favorite_ids = Favorite.objects.filter(
            user=request.user
        ).values_list('product_id', flat=True)

    return render(request, 'shop/product_detail.html', {
        'product': product,
        'categories': categories,
        'favorite_ids': favorite_ids,
    })

@login_required
def create_checkout_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})
    if not cart:
        return redirect('shop:cart')

    products = Product.objects.filter(id__in=cart.keys())

    line_items = []

    for product in products:
        quantity = cart[str(product.id)]
        line_items.append({
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': product.title,
                },
                'unit_amount': product.price * 100,  # Stripe работает в центах
            },
            'quantity': quantity,
        })

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=request.build_absolute_uri(
            reverse('shop:payment_success')
        ),
        cancel_url=request.build_absolute_uri(
            reverse('shop:checkout')
        ),
    )

    return redirect(session.url)
