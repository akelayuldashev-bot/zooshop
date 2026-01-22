from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:slug>/', views.category_products, name='category_products'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    path('cart/', views.cart, name='cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),

    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html',  authentication_form=LoginForm),
         name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),

    path('favorites/', views.favorites, name='favorites'),
    path('favorite/add/<int:product_id>/', views.add_to_favorite, name='add_to_favorite'),
    path('favorite/remove/<int:product_id>/', views.remove_from_favorite, name='remove_from_favorite'),

    path('checkout/', views.checkout, name='checkout'),
    path('payment_success/', views.payment_success, name='payment_success'),

    path('profile/', views.profile_view, name='profile'),

    path('product/<slug:slug>/', views.product_detail, name='product_detail'),

    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),


]
