"""RailJatri URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import home.views as home_view
import booking_tick.views as search
import payment_method.views as pay_method

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',home_view.home_page,name='home'),
    path('search_tick',search.booking_ticket,name='search_tick'),
    path('select_seat',search.seat_select,name='select_seat'),
    path('success',search.succesful,name='success'),
    path('tick_det',search.tick_details,name='tick_det'),
    path('bkash_pay',pay_method.bkash,name='bkash_pay'),
    path('card_pay',pay_method.card,name='card_pay'),
    path('nexus_pay',pay_method.nexus,name='nexus_pay'),
    path('pay_select',pay_method.pay_cat,name='pay_select'),
    path('rocket_pay',pay_method.rocket,name='rocket_pay'),
]
