from django import forms
from django.db import models

# Create your models here.
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import RowRange
from django.forms import widgets
from django.forms.widgets import Textarea, Widget
from django.contrib.auth.models import(AbstractBaseUser,BaseUserManager)
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,email,password=None,is_active=True,is_staff=False,is_admin=False):
        if not email:
            raise ValueError("Users must have email")
        
        if not password:
            raise ValueError("Users must have password")
        user_obj=self.model(
            email=self.normalize_email(email)
        )
        user_obj.staff=is_staff
        user_obj.admin=is_admin
        user_obj.active=is_active
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj
    
    def create_staffuser(self,email,password=None):
        user=self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user
    
    def create_superuser(self,email,password=None):
        user=self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user




class User(AbstractBaseUser):
    image=models.ImageField(default="deafult.jpg")
    email=models.EmailField(unique=True,max_length=255,verbose_name="email")
    active=models.BooleanField(default=True)
    staff=models.BooleanField(default=False)
    admin=models.BooleanField(default=False)
    timestamp=models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD='email'# in place of username
    REQUIRED_FIELDS=[]# username_field and password are there by default
    
    objects=UserManager()
    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True

    
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active
    
    @property
    def is_admin(self):
        return self.admin



#DataFlair Models
class Book(models.Model):
    name = models.CharField(max_length = 50)
    complete=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    hardness=models.IntegerField(null=False,blank=True,default=0)
    description=models.TextField(null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.name

