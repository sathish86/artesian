from django import forms
from integrator.models import UserProfile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    # Used for registration form
    email = forms.EmailField(required=True, max_length=254, help_text='Enter your email id')
    role = forms.CharField(max_length=15,
                           widget=forms.Select(choices=UserProfile.ROLE_CHOICES[:-1]),
                           required=True)
    description = forms.CharField(max_length=100, required=False, help_text='Description about you')

    class Meta:
        model = User
        fields = (
            'role',
            'description',
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'email'
        )

    def save(self, commit=True):
        # assign value to User model attributes
        user = super(RegistrationForm, self).save(commit=False)
        # assign value to UserProfile model attributes
        user_profile = UserProfile(user=user,
                                   description=self.cleaned_data['description'],
                                   role=self.cleaned_data['role'])

        if commit:
            # save user model
            user.save()
            # assign newly created user id to user profile model
            user_profile.user = user
            # save user profile model
            user_profile.save()

        return user, user_profile


class ProfileEditForm(UserChangeForm):
    # User profile edit form
    email = forms.EmailField(required=True, max_length=254, help_text='Enter your email id')
    role = forms.CharField(max_length=15,
                           widget=forms.Select(choices=UserProfile.ROLE_CHOICES[:-1]),
                           required=True)
    description = forms.CharField(max_length=100, required=False, help_text='Description about you')

    class Meta:
        model = User
        fields = (
            'role',
            'description',
            'first_name',
            'last_name',
            'password',
            'email'
        )

    def save(self, commit=True):
        # assign value to User model attributes
        user = super(ProfileEditForm, self).save(commit=False)
        user.userprofile.role = self.cleaned_data['role']
        user.userprofile.description = self.cleaned_data['description']

        if commit:
            # save user model
            user.save()
            user.userprofile.save()

        return user
