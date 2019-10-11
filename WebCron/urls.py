"""WebCron URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from CronJob import views

'''
_urlpatterns = [
    #path('polls', include('CronJob.tut_urls')),
    path('', views.index, name='index'),
    path('admin', admin.site.urls),

    #   path('login_test/', include('django.contrib.auth.urls')),


]
'''

urlpatterns = [
    # path('', views.index),
    path('admin/', admin.site.urls, name='admin'),

    # CronJob app urls
    path('', include('CronJob.urls')),

    # Test path for testing / experimenting
    path('test/', views.test, name='test'),
]
