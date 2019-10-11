from django.shortcuts import render, redirect
from django.contrib.auth.models import UserManager

from django.contrib.admin import forms

from django.contrib.auth import views as auth_views, logout
from django.contrib.auth import forms as auth_forms

# Main index view
from CronJob.forms import AddressForm


def index(request):
    login_form = ""  # auth_forms.

    context = {

    }

    if request.user.is_authenticated:
        # UserManager.create_user()
        # request.POST[0]
        return render(request, 'cronjob/create.html', context)
    else:
        return render(request, 'registration/login.html', context)
        # return redirect('login')

        # return login(request)
        # return auth_views.LoginView.as_view()
        # return auth_views.LoginView.as_view()


# Login view
def login_user(request):
    # register_form = forms.AuthenticationForm(request.POST or None)
    # register_form = forms.AuthenticationForm(data=request.POST)
    login_form = ""  # auth_forms.

    context = {
        'form': login_form
    }

    return render(request, 'registration/login.html', context)


# Login view
def logout_user(request):
    logout(request)
    # messages.success(request, 'Sie haben sich abgemeldet. 🦄 ')
    return redirect('home')


# Register view
def register_user(request):
    return render(request, 'registration/register.html', {})


# Cron fill view
def cron_fill(request):
    return ""


# test view for testing / experimentig
def test(request):
    test_form = auth_forms.UserCreationForm

    context = {
        'form': test_form
    }

    return render(request, 'registration/register.html', context)
