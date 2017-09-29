from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    ROLE_CHOICES = (
        ('government', 'Government'),
        ('investor', 'Investor'),
        ('startup', 'Startup'),
        ('corporate', 'Corporate'),
    )
    role = models.CharField(
        max_length=15,
        choices=ROLE_CHOICES,
        null=False
    )
