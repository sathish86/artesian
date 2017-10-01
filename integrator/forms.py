from django import forms
from integrator.models import UserProfile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
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
        user = super(RegistrationForm, self).save(commit=False)
        user_profile = UserProfile(user=user,
                                   description=self.cleaned_data['description'],
                                   role=self.cleaned_data['role'])

        if commit:
            user.save()
            user_profile.user = user
            user_profile.save()

        return user, user_profile

    # class UserEditForm(UserChangeForm):
    #     class Meta:
    #         model = User
    #         fields = ('first_name', 'last_name', 'email', 'password')
    #
    # class ProfileEditForm(forms.ModelForm):
    #     class Meta:
    #         model = UserProfile
    #         fields = ('role', 'description')


    # def save(self, commit=True):
    #     import pdb; pdb.set_trace()
    #     user = super(ProfileEditForm, self).save(commit=False)
    #     user.userprofile.role = self.cleaned_data['role']
    #     user.userprofile.description = self.cleaned_data['description']
    #     # user_profile = user.userprofile(
    #     #                 description=self.cleaned_data['description'],
    #     #                 role=self.cleaned_data['role'])
    #
    #     if commit:
    #         user.save()
    #         # user_profile.user = user
    #         # user_profile.save()
    #
    #     return user


class ProfileEditForm(UserChangeForm):
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
        user = super(ProfileEditForm, self).save(commit=False)
        user.userprofile.role = self.cleaned_data['role']
        user.userprofile.description = self.cleaned_data['description']

        if commit:
            user.save()
            user.userprofile.save()

        return user
