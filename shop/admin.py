from django.contrib import admin
from .models import Category, Product, Favorite


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'category', 'price', 'discount')
    list_filter = ('category',)
    search_fields = ('title',)

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')
    search_fields = ('user__username', 'product__title')
