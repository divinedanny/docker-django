from django.contrib import admin
from .models import UserAccount, VerifyUserOtp

# Register your models here.
admin.site.register(UserAccount)
admin.site.register(VerifyUserOtp)