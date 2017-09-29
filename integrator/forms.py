from django import forms
from integrator.models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    role = forms.CharField(max_length=15,
                           widget=forms.Select(choices=UserProfile.ROLE_CHOICES),
                           required=True)
    description = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = (
        'role',
        'description',
        'username',
        'first_name',
        'last_name',
        'password1',
        'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user_profile = UserProfile(user=user,
                        description=self.cleaned_data['description'],
                        role=self.cleaned_data['role'])

        if commit:
            user.save()
            user_profile.user = user
            user_profile.save()

        return user, user_profile
