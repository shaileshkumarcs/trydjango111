"""muypicky URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from django.contrib.auth.views import LoginView, PasswordResetView

from menus.views import HomeView
from profiles.views import ProfileFollowToggle



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name="home"),
    url('^login/$', LoginView.as_view(), name='login'),
    url(r'^profile-follow/$', ProfileFollowToggle.as_view(), name="follow"),
    #url('^password_reset_view/$', PasswordResetView.as_view(), name='password_reset'),
    url(r'^items/', include('menus.urls', namespace='menus')),
    url(r'^restaurants/', include('restaurants.urls', namespace='restaurants')),
    url(r'^u/', include('profiles.urls', namespace='profiles')),
    url(r'^about/$', TemplateView.as_view(template_name = 'about.html'), name="about"),
    url(r'^contact/$', TemplateView.as_view(template_name = 'contact.html'), name="contact"),

]

