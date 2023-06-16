from .models import Profile


class AuthBackend(object):
    supports_object_permissions = True
    supports_anonymous_user = False
    supports_inactive_user = False

    def get_user(self, user_id):
        try:
            return Profile.objects.get(pk=user_id)
        except Profile.DoesNotExist:
            return None

    def authenticate(self, request, username, password):
        try:
            user = Profile.objects.get(username=username)
        except Profile.DoesNotExist:
            return None
        
        return user if user.check_password(password) else None