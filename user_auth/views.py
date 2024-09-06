from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def user_login(request):
    """Renders the login page"""
    return render(request, 'authentication/login.html')


def authenticate_user(request):
    """Verifies the user's login credentials, then redirects them
    to the polls page if successful"""

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    # Reload the login page login is unsuccessful
    if user is None:
        print("None")
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    else:
        login(request, user)
        print("Verifying")
    return HttpResponseRedirect(
        reverse('user_auth:show_user')
    )


def show_user(request):
    """Renders the welcome page"""

    print(request.user.username)
    if request.user.username == "":
        return render(request, 'authentication/user.html')
    else:
        return render(request, 'authentication/user.html', {
            "username": request.user.username,
            "password": request.user.password})


def register(request):
    """Renders registration page and redirects user
    to login page if successful"""

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "Registration Successful! "
                                      "You may now log in.")
            return render(request, 'authentication/login.html')

    else:
        form = UserCreationForm()

    context = {"form": form}
    return render(request, "authentication/registration.html", context)