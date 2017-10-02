from django.shortcuts import render, redirect
from integrator.forms import RegistrationForm, ProfileEditForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse
from .models import Investor, Government, Corporate, Startup
import logging


# Create your views here.
def register(request):
    """
    Register a new user using form
    :param request: django http request object
    :return: redirects to home page, if its successful
    """
    logging.debug("Register view")
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('broadcast:home'))
        else:
            context = {'form': form}
            return render(request, 'integrator/registration_form.html', context)
    else:
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'integrator/registration_form.html', context)


def view_profile(request, pk=None):
    """
    View user profile
    :param request: django http request object
    :param pk: primary key of the user to get his/her detail
    :return: render a page to display profile detail
    """
    logging.debug("View profile")
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user

    args = {'user': user}
    return render(request, 'integrator/profile.html', args)


def edit_profile(request):
    """
    Edit user profile detail
    :param request: django http request object
    :return: render edit profile page for displaying errors or redirects to profile page
    """
    logging.debug("Edit profile")
    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('integrator:view_profile'))
    else:
        form = ProfileEditForm(instance=request.user)
        context = {'form': form}
        return render(request, 'integrator/profile_edit.html', context)


def change_password(request):
    """
    Used to change user password, it uses django's in built form to do change password.
    :param request: django http request object
    :return: redirects to profile page.
    """
    logging.debug("Change password")
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


def get_collaborator(request):
    """
    Create list of collaborator of a particular user and it depends on user role.
    :param request: django http request object
    :return: list of model objects
    """
    logging.debug("Get collaborators")
    collaborators = []
    # choose right model depends on user role
    if request.user.userprofile.role == "investor":
        try:
            user_obj = Investor.objects.get(current_user=request.user)
            collaborators = user_obj.users.all()
        except Investor.DoesNotExist:
            collaborators = None

    elif request.user.userprofile.role == "corporate":
        try:
            user_obj = Corporate.objects.get(current_user=request.user)
            collaborators = user_obj.users.all()
        except Corporate.DoesNotExist:
            collaborators = None

    elif request.user.userprofile.role == "startup":
        try:
            user_obj = Startup.objects.get(current_user=request.user)
            collaborators = user_obj.users.all()
        except Startup.DoesNotExist:
            collaborators = None

    elif request.user.userprofile.role == "government":
        try:
            user_obj = Government.objects.get(current_user=request.user)
            collaborators = user_obj.users.all()
        except Government.DoesNotExist:
            collaborators = None

    return collaborators


def list_collaborators(request):
    """
    List of users available to view and add them as collaborators to current user
    :param request: django http request object
    :return: list of user model objects
    """
    logging.debug("List collaborators")
    users = User.objects.all().exclude(id=request.user.id)
    collaborators = get_collaborator(request)
    return render(request, 'integrator/collaborators.html', {'users': users,
                                                             'collaborators': collaborators})


def change_collaboration(request, operation, pk):
    """
    Add or remove collaborators from current users based on operation requested.

    :param request: django http request object
    :param operation: used to find add or remove collaborator from current user
    :param pk: primary key of the user which will be added to current logged in user.
    :return: redirect to list of collaborators page.
    """
    logging.debug("Change collaborators")
    collaborate_user = User.objects.get(pk=pk)

    if operation == "add":
        # add user as collaborators to current user and choose right model based on the role.
        if request.user.userprofile.role == "investor":
            Investor.make_collaboration(request.user, collaborate_user)
        elif request.user.userprofile.role == "government":
            Government.make_collaboration(request.user, collaborate_user)
        elif request.user.userprofile.role == "corporate":
            Corporate.make_collaboration(request.user, collaborate_user)
        elif request.user.userprofile.role == "startup":
            Startup.make_collaboration(request.user, collaborate_user)

    elif operation == "remove":
        # remove user as collaborators from current user and choose right model based on the role.
        if request.user.userprofile.role == "investor":
            Investor.remove_collaboration(request.user, collaborate_user)
        elif request.user.userprofile.role == "government":
            Government.remove_collaboration(request.user, collaborate_user)
        elif request.user.userprofile.role == "corporate":
            Corporate.remove_collaboration(request.user, collaborate_user)
        elif request.user.userprofile.role == "startup":
            Startup.remove_collaboration(request.user, collaborate_user)

    return redirect("integrator:list_collaborators")
