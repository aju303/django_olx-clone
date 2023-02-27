from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    profile_pic=models.ImageField(null=True,upload_to="profile.images")
    address=models.CharField(max_length=500)
    phone=models.PositiveIntegerField()


class Products(models.Model):
    CATEGORY_CHOICES = (
        ('ELECTRONICS','ELECTRONICS'),
        ('fASHION','FASHION'),
        ('SPORTS','SPORTS'),
        ('HOME_DECOR','HOME_DECOR'),
        ('GADGETS','GADGETS')
    
    )
    name=models.CharField(max_length=200)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.CharField(max_length=500)
    condition=models.CharField(null=True,max_length=200)
    category=models.CharField(max_length=200,choices=CATEGORY_CHOICES)
    photo=models.ImageField(upload_to='product.images',null=True,blank=True)
    location=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10,decimal_places=3)
    options=(
        ("for sale","for sale"),
        ("exchange","exchange"),
        ("sold out","sold out"),
        ("rent","rent")
    )
    status=models.CharField(max_length=200,choices=options,default="for-sale")
    created_date=models.DateField(auto_now_add=True)


class Notifications(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    buyer=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.CharField(max_length=500)
    options=(
        ("sent","sent"),
        ("pending","pending"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=200,choices=options,default="sent")