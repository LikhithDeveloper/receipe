"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from home.views import *
from vege.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('', about, name="about"),
    path('about/', about, name="about"),
    path('', contact, name="contact"),
    path('contact/', contact, name="contact"),
    path('',receipe, name="receipe"),
    path('receipe/',receipe, name="receipe"),
    path('',delete_receipe,name="delete_receipe"),
    path('delete_receipe/<id>/',delete_receipe,name="delete_receipe"),
    path('',update_receipe,name="update_receipe"),
    path('update_receipe/<id>/',update_receipe,name="update_receipe"),
    path('login/',login_page, name="login_page"),
    path('',login_page, name="login_page"),
    path('',register_page, name="register_page"),
    path('register/',register_page, name="register_page"),
    path('',logout_page,name="logout_page"),
    path('logout/',logout_page,name="logout_page"),

   #path('success_page/',success_page,name="success_page"),


    path('admin/', admin.site.urls),
]  
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
