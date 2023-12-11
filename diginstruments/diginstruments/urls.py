"""
URL configuration for diginstruments project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from website.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_page, name='login'),
    path('register_page/', register_page),
    path('landing_page/', landing_page),
    path('guitarras_page/', guitarras_page),
    path('baterias_page/', baterias_page),
    path('violines_page/', violines_page),
    path('teclados_page/', teclados_page),
    path('flautas_page/', flautas_page),
    path('sax_page/', sax_page),
    path('log_out/', logout_page),
]
