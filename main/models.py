from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Notes(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    owners = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=False, blank=False)
    note = models.TextField()
    invited_user = models.ManyToManyField(User, blank=True, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    
    
