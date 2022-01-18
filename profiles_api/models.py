from django.db import models
#customizing django default user model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager



# Create your models here.


class UserProfileManager(BaseUserManager):
    """Manager for user profile"""
    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('user must have a email address')

        email = self.normalize_email(email)#second half of email all lower case
        user = self.model(email=email,name=name) #new model object

        user.set_password(password) #AbstractBaseUser fx haching password
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """New Super user"""
        user = self.create_user(email, name, password) #self autimatically pass for any class fx

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)   

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database Model for users in the System"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)#checking user is active or not
    is_staff = models.BooleanField(default=False) #check if user is a staff user or not i.e right to access Django Admin

    objects = UserProfileManager()#custom module manager for the objects to use with django CLI
    
    USERNAME_FIELD = 'email' #overrifing deafult username filed with email
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Get Full Name"""
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email