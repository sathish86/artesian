from django.contrib.auth.models import User
from integrator.models import Investor
from django.shortcuts import render, redirect

from django.views.generic import TemplateView
from broadcast.forms import HomeForm
from broadcast.models import Post
from django.contrib import messages


# Create your views here.
class HomeView(TemplateView):
    template_name = 'broadcast/home.html'

    def get(self, request):
        form = HomeForm()
        collaborators = []
        records = Post.latest_post.all()
        users = User.objects.all().exclude(id=request.user.id)
        if request.user.userprofile.role == "investor":
            try:
                user_obj = Investor.objects.get(current_user=request.user)
                collaborators = user_obj.users.all()
            except Investor.DoesNotExist:
                collaborators = None

        return render(request, self.template_name, {'form': form, 'records': records, 'users': users,
                                                    'collaborators': collaborators})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Your post was successfully created!')
            return redirect('broadcast:home')

        messages.warning(request, 'Please correct the error below.')  # <-
        users = User.objects.all().exclude(username=request.user)
        context = {'form': form, 'users': users}
        return render(request, self.template_name, context)
