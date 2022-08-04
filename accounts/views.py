from django.shortcuts import redirect, render
from .forms import UserForm
from django.contrib import messages
from .models import User


# Create your views here.

def registerUser(request): 
    if request.method =='POST':        
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