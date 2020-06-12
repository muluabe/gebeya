from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

from django.contrib.auth import get_user_model as user_model
User = user_model()

# ####################
##a CUSTOM USER and you are doing a ForeingKey to the Django User Model 
##( author = models.ForeignKey(User, related_name="courses") ) to get the 
##new User you can do this at the beginning of any file where you will use User
######################


# Create your models here.

class Product(models.Model):
    
    CONDITION_TYPE = (
        ("New", "New"),
        ("Used", "Used")
    )
    title = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, null=True)
    region = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=500)
    condition = models.CharField(max_length=100, choices=CONDITION_TYPE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2, default=0.00)
    created = models.DateTimeField(default=timezone.now)
    posted_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
        
class ProductImages(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    image_main = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, null=True)
    image_1 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, null=True) #Optional extra photos
    image_2 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, null=True)
    image_4 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, null=True)
    image_5 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, null=True)
    image_6 = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'
        
           
class Category(models.Model):
    ## for product category
    category_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category/' , blank=True , null=True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories' 
      
    def __str__(self):
        return self.category_name


class Brand(models.Model):
    ## for product brand
    brand_name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands' 
      
    def __str__(self):
        return self.brand_name