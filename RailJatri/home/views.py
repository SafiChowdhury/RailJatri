from django.shortcuts import render,redirect
# from home.models import login_details
# from create_acc.models import passenger
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.contrib import messages
from home.forms import (
    loginUser,
    ResetPasswordForm)
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetConfirmView
    
)
from home.forms import (
    ResetPasswordConfirmForm
)
# Create your views here.

def home_page(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('search_tick')
    context = {}

    return render(request,'login.html')

class SendEmailToResetPassword(PasswordResetView):
    template_name = 'password_reset.html'
    form_class = ResetPasswordForm

    # form_class = ResetPasswordConfirmForm
    # success_url = reverse_lazy('login')

    # def form_valid(self, form):
    #     messages.success(self.request, "Password reset successfully !")
    #     return super().form_valid(form)

class ResetPasswordConfirm(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    form_class = ResetPasswordConfirmForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, "Password reset successfully !")
        return super().form_valid(form)



