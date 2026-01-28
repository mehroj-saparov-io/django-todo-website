from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View

from .models import Task
from .forms import CustomUserCreationForm, LoginForm, TaskForm

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


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("profile")
    else:
        form = TaskForm()
    return render(request, "tasks/task_form.html", {"form": form})

@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/task_form.html", {"form": form})

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect("profile")
    return render(request, "tasks/task_confirm_delete.html", {"task": task})
