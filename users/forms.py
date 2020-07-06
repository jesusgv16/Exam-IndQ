from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

from django import forms
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    gender= forms.ChoiceField(widget=forms.RadioSelect, choices=[('M','Male'),('F','Female')])

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2','gender', )


