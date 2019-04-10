"""russian_troll_detector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from website.views import index, predict, visualize_account_details, home
from django.urls import path, include # new

urlpatterns = [
    url(r'^$', home),
    url(r'^oauth/complete/twitter/$', index),
    url(r'^predict', predict),
    url(r'^admin/', admin.site.urls),
    url(r'^details/', visualize_account_details),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
]



