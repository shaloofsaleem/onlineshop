# from distutils.command.upload import upload
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    def __str__(self) :
        return self.name

class Sub_Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE) 

    def __str__(self) :
        return self.name   

class Brand(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self) :
        return self.name 



class Product(models.Model):
    Availability=(('In stock','In stock'),('out of Stock','Out of Stock'))
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    image=models.ImageField(upload_to='ecomerce/pimg')
    desc=models.TextField()
    stock=models.IntegerField()
    price=models.IntegerField()
    Date=models.DateField(auto_now_add=True) 
    Availability=models.CharField(choices=Availability,null=True,max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=False,default='')  
    sub_category=models.ForeignKey(Sub_Category,on_delete=models.CASCADE,null=False,default='') 
    brands=models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
     


    def __str__(self) :
        return self.name   


class Contact_us(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.TextField()


    def __str__(self) :
        return self.name 

class order(models.Model):
    image=models.ImageField(upload_to='ecommerce/order/image')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.CharField(max_length=5)
    price=models.IntegerField()
    address=models.TextField()
    phone=models.CharField(max_length=100)
    pincode=models.CharField(max_length=100)
    date=models.DateField(default=datetime.datetime.today)


    def __str__(self) :
        return self.product.name 

    

