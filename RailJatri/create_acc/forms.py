from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUser(UserCreationForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'required':'',
            'name': 'frst',
            'id': 'name',
            'type':'text',
            'class':'form-control item',
            'placeholder': 'John',
            'maxlength':'25',
        })
        self.fields['last_name'].widget.attrs.update({
            'required':'',
            'name': 'last',
            'id': 'name-3',
            'type':'text',
            'class':'form-control item',
            'placeholder': 'Doe',
            'maxlength':'25',
        })
        self.fields['username'].widget.attrs.update({
            'required':'',
            'name': 'username',
            'id': 'name-3',
            'type':'text',
            'class':'form-control item',
            'placeholder': 'John1234',
            'maxlength':'16',
        })
        self.fields['email'].widget.attrs.update({
            'required':'',
            'name': 'email',
            'id': 'name-3',
            'type':'email',
            'class':'form-control item',
            'placeholder': 'johndoe@mail.com',
            'maxlength':'40',
        })
        self.fields['password1'].widget.attrs.update({
            'required':'',
            'name': 'password1',
            'id': 'name-3',
            'type':'password',
            'class':'form-control item',
            'placeholder': 'Password',
            'maxlength':'20',
        })
        self.fields['password2'].widget.attrs.update({
            'required':'',
            'name': 'password2',
            'id': 'name-3',
            'type':'password',
            'class':'form-control item',
            'placeholder': 'Confirm Password',
            'maxlength':'20',
        })
        
    class Meta:
        model = User
        fields=['first_name','last_name','username','email','password1','password2',]