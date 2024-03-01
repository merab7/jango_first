from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from .forms import SignUpForm, Add_form
from .models import Record

def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})

    








def logout_user(request):
    logout(request)
    messages.success(request, "You Have Logged Out")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered")
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form':form})


def costumer_record(request, pk):
    if request.user.is_authenticated:
        costumer_record  = Record.objects.get(id=pk)
        return render(request, 'record.html', {'costumer_record':costumer_record})
    else:
            messages.success(request, "You Must be Logged In")
            return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Record deleted successfully')
        return redirect('home')
    else :
        messages.success(request,'You need to Login first')
        return redirect('home')

def add_record(request):
        add_form = Add_form(request.POST or None)
        if request.user.is_authenticated:
            if request.method == 'POST':
                if add_form.is_valid():
                    add_form.save()
                    messages.success(request, "Record Added...")
                    return redirect('home')
          
            return render(request, 'add_record.html', {'add_form':add_form})
        else:
            messages.success(request, "You Must be Logged In...")
            return redirect('home')
        

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = Add_form(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record updated successfully')
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else :
        messages.success(request,'You need to Login first')
        return redirect('home')

        
