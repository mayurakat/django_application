import email
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager,PermissionsMixin



# Create your models here




class UserManager(BaseUserManager):
    def create_user(self, email, name,DOB, mobile,password=None):
        
        user = self.model(name=name,mobile=mobile,DOB=DOB,email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name,DOB, mobile,password):
        user = self.create_user(
            email=email, password=password, DOB=DOB,name=name,mobile=mobile)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user





class User(AbstractBaseUser,PermissionsMixin):
    name = models.CharField('Full Name',max_length=255,null=True,blank=True)
    email = models.EmailField(max_length=255,unique=True)
    mobile = models.BigIntegerField()
    DOB = models.DateField(max_length=8,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','mobile']

    def __str__(self):
        return "{}".format(self.name)