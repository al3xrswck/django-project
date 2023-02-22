from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=35, label='Username')
    password = forms.CharField(min_length=10, max_length=128, label='Password', widget=forms.PasswordInput)