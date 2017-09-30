from django.shortcuts import render, redirect
from integrator.forms import RegistrationForm, ProfileEditForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse
from django.views.generic import TemplateView
# Create your views here.

#
# def home(request):
#     return render(request, 'integrator/home.html')


class HomeView(TemplateView):
    template_name = 'integrator/home.html'


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('integrator:home'))
        else:
            context = {'form': form}
            return render(request, 'integrator/registration_form.html', context)
    else:
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'integrator/registration_form.html', context)

def view_profile(request):
    args = {'user_value': request.user}
    return render(request, 'integrator/profile.html', args)


def edit_profile(request):
    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('integrator:view_profile'))
    else:
        form = ProfileEditForm(instance=request.user)
        context = {'form': form}
        return render(request, 'integrator/profile_edit.html', context)


# def edit_profile(request):
#     if request.method == "POST":
#         user_form = UserEditForm(request.POST, instance=request.user)
#         profile_form = ProfileEditForm(request.POST, instance=request.user.userprofile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             # messages.success(request, _('Your profile was successfully updated!'))
#             return redirect(reverse('view_profile'))
#         # else:
#         #     messages.error(request, _('Please correct the error below.'))
#     else:
#         user_form = UserEditForm(request.POST, instance=request.user)
#         profile_form = ProfileEditForm(request.POST, instance=request.user.userprofile)
#         context = {'user_form': user_form, 'profile_form': profile_form}
#         return render(request, 'integrator/profile_edit.html', context)


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('integrator:view_profile'))
        else:
            context = {'form': form}
            return render(request, 'integrator/password_change.html', context)
    else:
        form = PasswordChangeForm(user=request.user)
        context = {'form': form}
        return render(request, 'integrator/password_change.html', context)
