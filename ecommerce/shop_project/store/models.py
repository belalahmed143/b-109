from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Banner(models.Model):
    title  = models.CharField(max_length = 150)
    image = models.ImageField(upload_to = 'BannerImage')
    http_link  = models.URLField(max_length = 400, blank=True, null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name  = models.CharField(max_length = 150)
    parent  = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='child')
    image = models.ImageField(upload_to='CategoryImage')

    def __str__(self):
        return self.name

class Brand(models.Model):
    name  = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='CategoryImage')

    def __str__(self):
        return self.name

class PriceRange(models.Model):
    pricerange  = models.CharField(max_length = 150)

    def __str__(self):
        return self.pricerange    

class Product(models.Model):
    name = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='ProductImage')
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)
    description  = models.TextField()
    post_date = models.DateField(auto_now=False, auto_now_add=False)
    category  = models.ForeignKey(Category, on_delete=models.CASCADE)
    barnd  = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    price_range  = models.ForeignKey(PriceRange, on_delete=models.CASCADE, blank=True, null=True)
    
    

    def __str__(self):
        return self.name
    

class CartProduct(models.Model):
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered  = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return self.product.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct)
    ordered  = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    
    def __str__(self):
        return self.user.username
    
    
    
    
    