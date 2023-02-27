from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView,FormView,TemplateView,ListView,DetailView
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from seller.models import UserProfile,Products
from seller.forms import RegistrationForm,LoginForm,UserProfileForm,ProductForm
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator

# Create your views here.

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"invalid session")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

decs=[signin_required,never_cache]


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
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("home")
            else:
                messages.error(request,"invalid credentials")
                return render(request,"login.html",{"form":form})



class HomeView(ListView):
    template_name="home.html"
    context_object_name="products"
    model=Products

@method_decorator(decs,name="dispatch")
class UserProfileView(TemplateView):
    template_name="user-profile.html"
   
@method_decorator(decs,name="dispatch")
class UserEditView(CreateView):
    template_name="edituser.html"
    form_class=UserProfileForm
    success_url=reverse_lazy('userdetails')


    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"user details have been updated")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request,"couldnt update user details")
        return super().form_invalid(form)


@method_decorator(decs,name="dispatch")
class ProductAddView(CreateView):
    template_name="sellproducts.html"
    form_class=ProductForm
    success_url=reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"Product has been added to sell")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request,"couldnt add product")
        return super().form_invalid(form)



class ProductdetailView(DetailView):
    template_name="productdetail.html"
    context_object_name="products"
    pk_url_kwarg="id"
    model=Products


decs
def logout_view(request,*args,**kwargs):
    logout(request)
    messages.success(request,"logged out")
    return redirect("signin")
