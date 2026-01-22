from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


#Категории товаров, товары, связь товаров, изо товаров
class Category(models.Model):
    name = models.CharField(max_length=240)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=240)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField(blank=True)
    price = models.IntegerField()
    discount = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

#=======================================================
#Izbrannoe

class Favorite(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='favorites'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='favorite_by'
    )

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f'{self.user} ♥ {self.product}'



class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username


