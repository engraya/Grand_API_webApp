from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile
from django_countries.fields import CountryField


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'id' : 'user',
            'type' : 'text',
            'class' : 'input',
            'placeholder' : 'Enter your First Name'
        })
        self.fields['last_name'].widget.attrs.update({
            'id' : 'user',
            'type' : 'text',
            'class' : 'input',
            'placeholder' : 'Enter your Last Name'
        })
        self.fields['username'].widget.attrs.update({
            'id' : 'user',
            'type' : 'text',
            'class' : 'input',
            'placeholder' : 'Choose your Username Name'
        })
        self.fields['email'].widget.attrs.update({
            'id' : 'user',
            'type' : 'text',
            'class' : 'input',
            'placeholder' : 'Enter your Email Address here'
        })
        self.fields['password1'].widget.attrs.update({
            'id' : 'user',
            'type' : 'text',
            'class' : 'input',
            'data-type' : 'password',
            'placeholder' : 'Enter your Password here'
        })
        self.fields['password2'].widget.attrs.update({
            'id' : 'user',
            'type' : 'text',
            'class' : 'input',
            'data-type' : 'password',
            'placeholder' : 'Confirm your Password here'
        })
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password1 = forms.CharField(max_length=100)
    password2 = forms.CharField(max_length=100)


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id' : 'user', 'type' : 'text', 'class':'input','placeholder': 'Enter Your Username here'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id' : 'user', 'type' : 'text', 'class': 'input', 'data-type' : 'password', 'placeholder': 'Enter Your Password here'}))



class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.EmailField(max_length=100, required=True, widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'id' : 'user',
            'type' : 'email',
            'class' : 'form-control',
            'value' : ''
        })
        self.fields['username'].widget.attrs.update({
            'id' : 'user',
            'type' : 'username',
            'class' : 'form-control',
            'value' : ''
        })

    class Meta:
        model = User
        fields = ['email', 'username']


class UserProfileUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fullName'].widget.attrs.update({
            'id' : 'profile',
            'type' : 'text',
            'name' : 'fullName',
            'class' : 'form-control',
            'value' : ''
        })
        self.fields['phone'].widget.attrs.update({
            'id' : 'profile',
            'type' : 'text',
            'name' : 'phone',
            'class' : 'form-control',
            'value' : ''
        })
        self.fields['profession'].widget.attrs.update({
            'id' : 'profile',
            'type' : 'text',
            'name' : 'profession',
            'class' : 'form-control',
            'value' : ''
        })
        self.fields['bio'].widget.attrs.update({
            'id' : 'profile',
            'type' : 'text',
            'name' : 'bio',
            'class' : 'form-control',
            'value' : ''
        })
        self.fields['country'].widget.attrs.update({
            'id' : 'profile',
            'type' : 'select',
            'name' : 'country',
            'class' : 'form-control',
            'value' : ''
        })


    fullName = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=100)
    profession = forms.CharField(max_length=100)
    country = CountryField()
    profile_pic = forms.ImageField()
    bio = forms.CharField()

    class Meta:
        model = Profile
        fields =  ['fullName', 'bio', 'phone', 'profile_pic', 'country', 'profession']

