"""ConcentrateWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

from . import views

app_name = 'concentrate'
urlpatterns = [
    url(r'^$', views.concentrate, name='concentrate'),
    url(r'^results/([a-zA-Z]{25})/([r|w|b]{25})', views.results, name='results'),
    url(r'^results1/([a-zA-Z]{25})/([r|w|b]{25})/(.*)', views.results1, name='results1'),
    url(r'^results2/([a-zA-Z]{25})/([r|w|b]{25})/(.*)', views.results2, name='results2'),
    url(r'^results3/([a-zA-Z]{25})/([r|w|b]{25})/(.*)/(.*)', views.results3, name='results3'),                    
    url(r'^search', views.search, name='search'),
]
