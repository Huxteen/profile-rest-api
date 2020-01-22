from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
# Create your models here.


class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model. """

    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address.')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password, **extra_fields):
        """Create and save a new super user."""

        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """User profiles we want to collect. """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        '''Returns the full name, with a space in between.'''
        return self.name.strip()

    def get_short_name(self):
        '''Returns the short name for the user.'''
        return self.name.strip()

    def __str__(self):
        """ Django uses this when it need to convert the object to a string """
        return self.email






class ProfileFeedItem(models.Model):
    """ Profile Status update."""

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string."""

        return self.status_text
