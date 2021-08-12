from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
def log_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request,"شماره موبایل یا رمز عبور نادرست است.")
            return redirect("/")
def log_out(request):
    logout(request)
    return redirect("/")
# Create your views here.
