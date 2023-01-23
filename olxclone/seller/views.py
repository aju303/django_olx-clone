from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView,FormView,TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from seller.models import UserProfile
from seller.forms import RegistrationForm,LoginForm

# Create your views here.

class SignUpView(CreateView):
    template_name="signup.html"
    form_class=RegistrationForm
    success_url= reverse_lazy("signin")

    def form_valid(self, form):
        messages.success(self.request,"account has been created successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request,"account creation failed")
        return super().form_invalid(form)


class SigninView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            mail=form.cleaned_data.get("emailaddress")
            pwd=form.cleaned_data.get("password")
            em=object.filter.get
            usr=authenticate(request,emailaddress=mail,password=pwd)
            if usr:
                login(request,usr)
                return redirect("home")
            else:
                messages.error(request,"invalid credentials")
                return render(request,"login.html",{"form":form})


class HomeView(TemplateView):
    template_name="home.html"