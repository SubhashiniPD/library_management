from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Student


def register(request):

    if request.method == "POST":

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        phone = request.POST["phone"]
        department = request.POST["department"]

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {
                "error": "Username already exists. Please choose another username."
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        Student.objects.create(
            user=user,
            phone=phone,
            department=department
        )

        return redirect("login")

    return render(request, "register.html")


def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        return render(request, "login.html", {
            "error": "Invalid username or password"
        })

    return render(request, "login.html")


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")
