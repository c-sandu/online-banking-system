from django.contrib.auth.forms import AuthenticationForm

from django import forms
from banking.models import User

class LoginForm(AuthenticationForm):
    auth_code = forms.CharField()

    def confirm_login_allowed(self, user):
        auth_code = self.request.POST['auth_code']
        if not user.check_auth_code(auth_code):
            raise forms.ValidationError(
                "This account is inactive.",
                code='inactive',
            )