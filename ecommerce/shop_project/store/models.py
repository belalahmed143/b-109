from django.db import models
from django.contrib.auth.models import User
from payment_app.models import ShipingAddress
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

    def subtotal(self):
        if self.product.discount_price:
            return self.product.discount_price * self.quantity
        else:
            return self.product.price * self.quantity



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct)
    ordered  = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)
    Payment_Method =(
        ('Cash on delivery','Cash on delivery'),
        ('Bkash','Bkash'),
    )
    payment_option  = models.CharField(max_length = 150, choices=Payment_Method,blank=True, null=True)
    shiping_address  = models.ForeignKey(ShipingAddress, on_delete=models.CASCADE,blank=True, null=True)
    
    

    
    def __str__(self):
        return self.user.username

    def get_total(self):
        sum = 0
        for i in self.products.all():
            sum += i.subtotal()
        return sum
        
    def get_final_total(self):
        return self.get_total() + 90
    
    
    
    
    