from .forms import RegisterForm
from django.shortcuts import render, redirect


# Create your views here.
def register(response):
    """
        A function for registering user
    """
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = RegisterForm()
    return render(response, "register/register.html",{"form":form})
