from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm

# Create your views here.

def dashboard(request):
    return render(request,'userapp/index.html')


def login(request):
    return render(request,'userapp/login.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('dashboard')
    
    context = {
        'form':form,
    }
    return render(request,'userapp/register.html',context)