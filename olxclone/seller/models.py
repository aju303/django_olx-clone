from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(null=True,upload_to="profile.images")
    address=models.CharField(max_length=500)
    phone=models.PositiveIntegerField()



class Category(models.Model):
    category_name=models.CharField(max_length=200)
    is_active=models.BooleanField(default=True)


class Products(models.Model):
    name=models.CharField(max_length=200)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.CharField(max_length=500)
    condition=models.CharField(null=True,max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    location=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    options=(
        ("for sale","for sale"),
        ("exchange","exchange"),
        ("sold out","sold out"),
        ("rent","rent")
    )
    status=models.CharField(max_length=200,choices=options,default="for-sale")
    created_date=models.DateField(auto_now_add=True)


class ProductImages(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    image=models.ImageField(null=True,upload_to="product.images")



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