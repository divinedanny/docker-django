from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
import uuid
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserManger(BaseUserManager):
    def create_user(self, email, password, firstname, lastname, **other_fields):
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            firstname=firstname,
            lastname=lastname,
            **other_fields
        )
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, password, firstname, lastname, **other_fields):
        
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_verified', True)
        
        return self.create_user(email, password, firstname, lastname, **other_fields)
        
    
class UserAccount(AbstractBaseUser, UserManger):
    
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True,
                          editable=False,
                          unique=True
                          )
    email = models.EmailField(_('email'), 
                              blank=False, 
                              null=False
                              )
    firstname = models.CharField(_('firstname'), 
                                 blank=False, 
                                 null=False
                                 )
    lastname = models.CharField(_('lastname'), 
                                blank=False, 
                                null=False
                                )
    
    date_created = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False
    )
    date_updated = models.DateTimeField(
        auto_now=True,
        null = False,
        blank=False
    )
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']
    
    objects = UserManger()
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = self.set_uuid()
        self.full_clean()
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return super().__str__(self.email)
    
    
class VerifyUserOtp(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(
        UserAccount, related_name="activationtoken", on_delete=models.CASCADE, null=True)
    otp = models.CharField(_("Token"), max_length=6, null=False, blank=False)
    # date_issued = models.DateTimeField(auto_now_add=True)


        
        
        