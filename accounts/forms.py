from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label='',
        max_length=80, 
        required=True,
        widget=forms.TextInput(
            attrs={
                "placehoder":"Enter your first name",
                })),
    last_name = forms.CharField(
        label='',
        max_length=80, 
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Enter your last name"
            }
        )),
    email = forms.EmailField(
        label='',
        max_length=280, 
        error_messages={'required':"Invalid email"}, 
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder":"Enter your Email",
                }))
    username = forms.CharField(
        label='',
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Enter your username',
            }
        )
    )
    password1 = forms.CharField(
        label='',
        max_length=30,
        min_length=8,
        help_text="must be at leat 8 characters",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": 'Enter your password',
            }
        )
    )
    password2 = forms.CharField(
        label='',
        max_length=30,
         min_length=8,
        help_text="must be same as above",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm password"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')