"""
URL configuration for WebsiteForBusiness project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from financial_analyst.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page),
    path('about_us/', about_us),
    path('services/', services),
    path('cart/', cart),
    path('add/<int:service_id>/', add_to_cart, name='add'),
    path('add_yet/<int:item_id>/', add_to_cart_yet, name='add_yet'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove'),
    path('login/', login_view),
    path('register/', register_view),
    path('logout/', logout_view),
]
