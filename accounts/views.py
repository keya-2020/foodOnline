from django.shortcuts import redirect, render
from .forms import UserForm
from vendor.forms import VendorForm
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import User, UserProfile
from .utils import detectUser
from django.core.exceptions import PermissionDenied

# Restict the vendor from accessing the customer page
def check_role_vendor(user):
    if user.role ==1:
        return True
    else:
        raise PermissionDenied

# Restict the vendor from accessing the customer page
def check_role_customer(user):
    if user.role ==2:
        return True
    else:
        raise PermissionDenied

# Create your views here.

def registerUser(request): 
    if request.user.is_authenticated:
        messages.warning(request, 'you are already logged in.')
        return redirect('myAccount')       
    
    elif request.method =='POST':        
        form = UserForm(request.POST)
        
        if form.is_valid():
            #Create the user using the form
            # password = form.cleaned_data['password']
            """ user = form.save(commit=False)
            user.role = User.CUSTOMER
            user.set_password(password)
            user.save()               """

            # Create the user using method
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, 'your account has been registered sucessfully')
            return redirect('registerUser')
        else:
            
            # print("Invalid Form")
            #print(form.errors)
            return render(request, 'accounts/registerUser.html',{'form':form})
            

    else:
        form = UserForm()

    form = UserForm()
    context= {
        'form':form,
    }
    return render(request, 'accounts/registerUser.html',context)


def registerVendor(request):
    if request.user.is_authenticated:
        messages.warning(request, 'you are already logged in.')
        return redirect('myAccount') 
    elif request.method == 'POST':
        form = UserForm(request.POST)
        v_form = VendorForm(request.POST, request.FILES)
        
        if form.is_valid() and v_form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.VENDOR
            user.save()
            vendor = v_form.save(commit=False)
            vendor.user = user
            user_profile = UserProfile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save() 
            
            messages.success(request, 'your account has been registered sucessfully! please wait for the approval.')
            return redirect('registerVendor')
        
        else:
            print(form.errors)
            return redirect('registerVendor')
        
    else:
        form = UserForm()
        v_form= VendorForm()
    context = {
        'form': form,
        'v_form':v_form,
    }
    return render(request,"accounts/registerVendor.html", context)

def login(request):
    if request.user.is_authenticated:
        messages.warning(request, 'you are already logged in.')
        return redirect('myAccount')  
     
    elif request.method =='POST':        
            email= request.POST["email"]
            password= request.POST["password"]
            user = auth.authenticate(email=email, password=password)        

            if user is not None:
                auth.login(request,user)
                messages.success(request, 'you are now logged in.')
                return redirect('myAccount')
            else:
                messages.error(request, 'invalid login credentials.')
                return redirect('login')    
    return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    messages.info(request, 'you are now logged out')
    return redirect('home')

@login_required
def myAccount(request):
    user = request.user
    redirectUrl = detectUser(user)
    return redirect(redirectUrl)

@login_required
@user_passes_test(check_role_customer)
def custDashboard(request):
   return render(request, 'accounts/custDashboard.html')

@login_required
@user_passes_test(check_role_vendor)
def vendorDashboard(request):
   return render(request, 'accounts/vendorDashboard.html')
