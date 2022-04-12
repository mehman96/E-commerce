# forms import edirik
from django import forms
from django.forms import fields
from django.db import models
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation


# form yazdigimiz datalar bura dussun deye
User=get_user_model()

class RegisterterForm(UserCreationForm):
    # password1=forms.CharField(max_length=127,validators=[validate_password ],widget=forms.PasswordInput(attrs={
    # 'class ' : 'form-control',
    # 'placeholder': 'Password',
    # }),)

    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'New Password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control', 'placeholder': 'Confirm Password'}),
        strip=False,
        help_text=("Enter the same password as before, for verification."),
    )

   
    class Meta:
        model = User
        fields = (
            'first_name', 
            'last_name',
            'username',
            'email',
            'bio',
            'gender',
            'image',
        )

        widgets= {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'bio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bio', 'style':'margin-bottom:10px' }),


          
            # 'password1':forms.CharField(max_length=127,validators=[validate_password ],widget=forms.PasswordInput(attrs={'class ' : 'form-control', 'placeholder': 'Password',}),),
            # 'password2':forms.CharField(max_length=127,validators=[validate_password ],widget=forms.PasswordInput(attrs={'class ' : 'form-control', 'placeholder': 'Password',}),)
        }
        

        # iki kodun ust uste dusb dusmediyi yoxlamaq ucun
        # clean data - formdan gelen datalari ozunde saxliyir

    # def clean(self):
    #     password1=self.cleaned_data.get('password1')
    #     password2=self.cleaned_data.get('password2')

    #     if password1!=password2:
    #         raise forms.ValidationError("Parol sehvdir. Yeniden daxil edin")

    #     return super().clean()

class LoginForm(forms.Form):
    email=forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'E-mail'}
    ))
    password=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'password'}
    ))