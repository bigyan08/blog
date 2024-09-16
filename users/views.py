from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Your account is now created! You can login now!')
            return redirect('login')
    else:
        form=UserRegistrationForm()

    return render(request,'users/register.html',{'form':form})

def user_logout(request):
    logout(request)
    return render(request,'users/logout.html',{})

@login_required
def profile(request):
    return render(request,'users/profile.html')