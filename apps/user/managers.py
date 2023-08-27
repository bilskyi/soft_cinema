from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username=None, password=None, **kwargs):
        
        user = self.model(
            username=username,
            **kwargs
        )

        if kwargs.get('is_superuser'):
            user = self.model(
                username=username,
                **kwargs
            )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username, password, **kwargs):
        kwargs.setdefault('is_superuser', False)
        kwargs.setdefault('is_active', True)
        return self._create_user(username=username, password=password)
    
    def create_superuser(self, username, password, **kwargs):
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_superuser') is not True:
            raise ValueError('super user must have is_superuser=True')
        
        return self._create_user(username=username, password=password, **kwargs)