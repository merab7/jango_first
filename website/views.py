from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 

def home(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None :
            login(request, user)
            messages.success(request, "You have been Logged in")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in, please try again...")
            return redirect('home')
    else:

       return render(request, 'home.html', {})





def logout_user(request):
    logout(request)
    messages.success(request, "You Have Logged Out")
    return redirect('home')


def register_user(request):
    
    return render(request, 'register.html', {})

