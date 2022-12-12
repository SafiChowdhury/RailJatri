from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


class loginUser(UserCreationForm):
    class Meta:
        model = User
        fields=['email','password1']

class ResetPasswordForm(PasswordResetForm):
    # new_password1 = forms.CharField(
    #     max_length=150,
    #     widget=forms.PasswordInput
    # )
    # new_password2 = forms.CharField(
    #     max_length=150,
    #     widget=forms.PasswordInput
    # )

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
    
    def send_mail(self, subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name) -> None:
        return super().send_mail(subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name)

class ResetPasswordConfirmForm(forms.Form):
    new_password1 = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput
    )
    new_password2 = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
        

    def clean_new_password1(self, *args, **kwargs):
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.data.get('new_password2')
        
        if new_password1 and new_password2:
            if new_password1 != new_password2:
                raise forms.ValidationError("Password mismatch")

        return new_password1

    def save(self, commit=True, *args, **kwargs):
        self.user.set_password(self.cleaned_data.get('new_password1'))

        if commit:
            self.user.save()

        return self.user