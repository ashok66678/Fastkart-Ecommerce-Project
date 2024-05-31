from django import forms
from .models import User as MyUser
from django.contrib import auth

class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(max_length=32, widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ['email', 'full_name', 'password', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('password fields didnot match')

