from django.contrib import admin
from seller.models import Products,UserProfile,Notifications

# Register your models here.

admin.site.register(Products)
admin.site.register(UserProfile)
admin.site.register(Notifications)