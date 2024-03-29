"""mysite URL Configuration

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
from django.urls import path, re_path
from myWeb.views import index, register,cancel, loggin_form, landing_page, formulario_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('', include('admin_material.urls')),
    path('admin/', admin.site.urls),
    path('', index, name='index'),    
    path('login/', loggin_form, name='login'),
    path('landing/', landing_page, name='landing'),
    path('formulario/', formulario_view, name='formulario'),
    path('register/', register, name='register'),
    path('register/cancel/', cancel, name='cancel'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


