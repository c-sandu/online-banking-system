from .models import User

class UserAuth(object):

    def authenticate(self, username=None, password=None, auth_code=None):
        try:
            user = User.objects.get(pk=username)
            if user.check_password(password):
                if user.check_auth_code(auth_code):
                    return user
        except User.DoesNotExist:
            return None

    def get_user(self, username):
        try:
            user = CustomUser.objects.get(pk=username)
            if user.is_active:
                return user
            return None
        except:
            User.DoesNotExist:
            return None