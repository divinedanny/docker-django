from django.db import models
import uuid
from accounts.models import UserAccount

# Create your models here.

class Notes(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    owner = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="owner", null = True)
    title = models.CharField(max_length=150, null=False, blank=False)
    note = models.TextField()
    invited_user = models.ManyToManyField(UserAccount, blank=True, related_name="invited_user")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    
    
