"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from csi import urls as csi_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^csi/', include(csi_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include


urlpatterns = [
    url('^markdown/', include( 'django_markdown.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'', include('csi.urls')),
]
