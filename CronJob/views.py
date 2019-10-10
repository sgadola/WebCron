from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import UserManager

# Main index view
def index(request):
    #   return HttpResponse("Hello, world. You're at the polls index.", {})

    context = {
        'Hello World': 'hello_world',
    }

    if request.user.is_authenticated:
        #UserManager.create_user()
        return render(request, 'cronjob/create.html', context)
    else:
        return render(request, 'cronjob/login.html', context)


# Login view
def login(request):
    context = {
        'register_form' : ''
    }

    return render(request, 'cronjob/login.html', {})


# Register view
def register(request):
    return render(request, 'cronjob/register.html', {})
