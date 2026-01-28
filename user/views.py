from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import CustomUserCreationForm, LoginForm

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})

class CustomLoginView(LoginView):
    template_name = "users/login.html"
    authentication_form = LoginForm

class CustomLogoutView(LogoutView):
    next_page = "login"
    allow_get = True

    def get(self, request, *args, **kwargs):
        print("Logout called for:", request.user)
        return super().get(request, *args, **kwargs)



@login_required
def profile(request):
    user = request.user
    tasks = user.tasks.all()
    return render(request, "users/profile.html", {"user": user, "tasks": tasks})

