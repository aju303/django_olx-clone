"""olxclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from seller import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register",views.SignUpView.as_view(),name="signup"),
    path("",views.SigninView.as_view(),name="signin"),
    path("home",views.HomeView.as_view(),name="home"),
    path("userdetails",views.UserProfileView.as_view(),name="userdetails"),
    path("user/edit_profile",views.UserEditView.as_view(),name="edit_user"),
    path("sell",views.ProductAddView.as_view(),name="sell"),
    path("product/detail/<int:id>",views.ProductdetailView.as_view(),name="detail"),
    path("user/signout",views.logout_view,name="signout")



    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
