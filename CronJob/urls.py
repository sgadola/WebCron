from django.urls import path, include
from . import views

# app_name = "CronJob"
urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('create/', views.create, name='create'),
    path('register/', views.register_user, name='register'),
]
