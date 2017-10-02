from django.contrib.auth.models import User
from django.db import models

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
        # this role won't be displayed in registration form or edit profile
        # form and it is for admin purpose.
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
    current_user = models.ForeignKey(User, related_name='investor_owner')
    contact_person = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    industry = models.CharField(max_length=100, null=True, blank=True)
    overall_budget = models.FloatField(null=True, blank=True)
    risk_appetite = models.CharField(max_length=100, null=True, blank=True)

    @classmethod
    def make_collaboration(cls, current_user, new_collaborator):
        """
        Add new user to currently logged in user

        :param current_user: currently logged in user id
        :param new_collaborator: new user id to be added.
        :return: None
        """
        if current_user.userprofile.role == 'investor':
            collaborator, created = Investor.objects.get_or_create(
                current_user=current_user
            )
            collaborator.users.add(new_collaborator)

    @classmethod
    def remove_collaboration(cls, current_user, new_collaborator):
        """
        Remove user from currently logged in user

        :param current_user: currently logged in user id
        :param new_collaborator: user id that need to be removed from currently logged in user
        :return: None
        """
        if current_user.userprofile.role == 'investor':
            collaborator, created = Investor.objects.get_or_create(
                current_user=current_user
            )
            collaborator.users.remove(new_collaborator)


class Government(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='govern_owner')
    contact_person = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    industry = models.CharField(max_length=100, null=True, blank=True)
    overall_budget = models.IntegerField(null=True, blank=True)
    market_capital = models.FloatField(null=True, blank=True)
    risk_appetite = models.CharField(max_length=100, null=True, blank=True)

    @classmethod
    def make_collaboration(cls, current_user, new_collaborator):
        """
        Add new user to currently logged in user

        :param current_user: currently logged in user id
        :param new_collaborator: new user id to be added.
        :return: None
        """
        if current_user.userprofile.role == 'government':
            collaborator, created = Government.objects.get_or_create(
                current_user=current_user
            )
            collaborator.users.add(new_collaborator)

    @classmethod
    def remove_collaboration(cls, current_user, new_collaborator):
        """
        Remove user from currently logged in user

        :param current_user: currently logged in user id
        :param new_collaborator: user id that need to be removed from currently logged in user
        :return: None
        """
        if current_user.userprofile.role == 'government':
            collaborator, created = Government.objects.get_or_create(
                current_user=current_user
            )
            collaborator.users.remove(new_collaborator)


class Startup(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='startup_owner')
    contact_person = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    industry = models.CharField(max_length=100, null=True, blank=True)
    no_of_employees = models.IntegerField(null=True, blank=True)

    @classmethod
    def make_collaboration(cls, current_user, new_collaborator):
        """
        Add new user to currently logged in user

        :param current_user: currently logged in user id
        :param new_collaborator: new user id to be added.
        :return: None
        """
        if current_user.userprofile.role == 'startup':
            collaborator, created = Startup.objects.get_or_create(
                current_user=current_user
            )
            collaborator.users.add(new_collaborator)

    @classmethod
    def remove_collaboration(cls, current_user, new_collaborator):
        """
        Remove user from currently logged in user

        :param current_user: currently logged in user id
        :param new_collaborator: user id that need to be removed from currently logged in user
        :return: None
        """
        if current_user.userprofile.role == 'startup':
            collaborator, created = Startup.objects.get_or_create(
                current_user=current_user
            )
            collaborator.users.remove(new_collaborator)


class Corporate(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='corporate_owner')
    contact_person = models.CharField(max_length=100, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    industry = models.CharField(max_length=100, null=True, blank=True)
    no_of_employees = models.IntegerField(null=True, blank=True)
    overall_budget = models.IntegerField(null=True, blank=True)
    market_capital = models.FloatField(null=True, blank=True)
    risk_appetite = models.CharField(max_length=100, null=True, blank=True)

    @classmethod
    def make_collaboration(cls, current_user, new_collaborator):
        """
        Add new user to currently logged in user

        :param current_user: currently logged in user id
        :param new_collaborator: new user id to be added.
        :return: None
        """
        if current_user.userprofile.role == 'corporate':
            collaborator, created = Corporate.objects.get_or_create(
                current_user=current_user
            )
            collaborator.users.add(new_collaborator)

    @classmethod
    def remove_collaboration(cls, current_user, new_collaborator):
        """
        Remove user from currently logged in user

        :param current_user: currently logged in user id
        :param new_collaborator: user id that need to be removed from currently logged in user
        :return: None
        """
        if current_user.userprofile.role == 'corporate':
            collaborator, created = Corporate.objects.get_or_create(
                current_user=current_user
            )
            collaborator.users.remove(new_collaborator)
