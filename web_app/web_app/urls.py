"""
URL configuration for web_app project.

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
from django.urls import path, include

from views import home, cart, about, checkout, contact, shop, thankyou, register, signup, orders, knives, gloves, guns, invalid, search, touch

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/register/", register, name="register"),
    path("accounts/submit/", signup, name="signup"),
    path('', home, name='home'),
    path('index/', home, name='home'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('cart/', cart, name='cart'),
    path('contact/', contact, name='contact'),
    path('shop/', shop, name='shop'),
    path('shop/knives', knives, name='knives'),
    path('shop/gloves', gloves, name='gloves'),
    path('shop/guns', guns, name='guns'),
    path('shop-single/', checkout, name='shop-single'),
    path('thankyou/', thankyou, name='thankyou'),
    path('orders/', orders, name='orders'),
    path('invalid', invalid, name='invalid'),
    path('search/', search, name='search'),
    path('touch/', touch, name='touch')
]
