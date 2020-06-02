from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    """Form to be used to log users in."""

    username = forms.CharField()
    """By using a widget of PasswordInput, we tell Django that we 
    want the field to have a type of 'password'."""
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    """Form used to register a new user."""

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        """Here we filter to check if we already have somebody in the 
        database with the form's username."""
        if User.objects.filter(email=email).exclude(username=username):
            raise ValidationError(u'Email address must be unique')
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            """If either password field is NOT filled in, we return a validation 
            error."""
            raise ValidationError(u'Please confirm your password')
        
        if password1 != password2:
            """If the passwords aren't equal, we return a validation error, to 
            ensure that accounts can't be registered under 2 seperate passwords."""
            raise ValidationError(u'Passwords must match')
        
        return password2