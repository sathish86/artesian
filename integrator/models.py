from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(role='investor')


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    ROLE_CHOICES = (
        ('government', 'Government'),
        ('investor', 'Investor'),
        ('startup', 'Startup'),
        ('corporate', 'Corporate'),
        ('artesian', 'Artesian'),
    )
    role = models.CharField(
        max_length=15,
        choices=ROLE_CHOICES,
        null=False
    )

    objects = models.Manager()  # The default manager.
    investor = UserProfileManager()

    def __str__(self):
        return self.user.username


class Investor(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner')

    @classmethod
    def make_collaboration(cls, current_user, new_collaborator):
        collaborator, created = Investor.objects.get_or_create(
            current_user=current_user
        )
        collaborator.users.add(new_collaborator)

    @classmethod
    def remove_collaboration(cls, current_user, new_collaborator):
        collaborator, created = Investor.objects.get_or_create(
            current_user=current_user
        )
        collaborator.users.remove(new_collaborator)
