from django.urls import path
from . import views

app_name = "CronJob"
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('', views.index, name='index'),


    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]