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

import list_trains.views as list

from django.contrib.auth import views as auth_views
import change_profile.views as change
import contactus.views as contactus
import create_acc.views as registraion
import forgetChangePass.views as forget
import forgetPass.views as passforget
import create_acc.views as views
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from home.views import (
    SendEmailToResetPassword,
    ResetPasswordConfirm
)

from change_profile.form import MyPasswordChangeForm

urlpatterns = [
    path('admin/', admin.site.urls),
    #login &  registraion
    path('',home_view.home_page,name='login'),
    path('registration/', registraion.registration, name='registration'),
    #ticket
    path('search_tick/',search.booking_ticket,name='search_tick'),
    path('select_seat/',search.seat_select,name='select_seat'),
    path('success/',search.succesful,name='success'),
    path('tick_det/',search.tick_details,name='tick_det'),
    path('bkash_pay/',search.bkash,name='bkash_pay'),
    #other pay_method
    path('pay_select/',search.pay_cat,name='pay_select'),
    path('rocket_pay/',pay_method.rocket,name='rocket_pay'),
    path('card_pay/',pay_method.card,name='card_pay'),
    path('nexus_pay/',pay_method.nexus,name='nexus_pay'),
    path('list_trains/',list.list_train,name='list_trains'),
    #user_profile
    path('upcoming/',change.journey_details,name='upcoming'),
    path('changenum/',change.changenum,name='changenum'),
    path('infoupdate/',change.updateInfo,name='infoupdate'),
    path('contactus/',contactus.contactus,name='contactus'),
    #password_chng
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='changepass.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='changepassword'),
    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'), name='passwordchangedone'),
    #for rest_pass
    path('password_reset/', SendEmailToResetPassword.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', ResetPasswordConfirm.as_view(), name='password_reset_confirm'),
]
