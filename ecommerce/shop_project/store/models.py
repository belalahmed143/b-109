from django.db import models

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
    
    
    
    
    
    
    
    