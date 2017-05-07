from django.contrib.auth.forms import AuthenticationForm

from django import forms

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        ceva = forms.CharField(label = 'anal', max_length=40)