from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager



class NewUser(AbstractBaseUser, PermissionsMixin):
    
    pass