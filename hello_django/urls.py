"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url

from users.views import signup_view, home_view, login_view, logout_view
from events.views import events_view, listEvents_view

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^users/$', signup_view, name='signup'),
    url(r'^users/login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^home/$', home_view, name='home'),
    url(r'^events/$', events_view, name='events'),
    url(r'^levents/$', listEvents_view, name='levents'),
    url(r'^$', home_view, name='home'),
    url(r'^accounts/login/$', login_view, name='login'),
 
]
