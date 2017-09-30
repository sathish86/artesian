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
        records = Post.objects.all()
        return render(request, self.template_name, {'form': form, 'records': records})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['post']
            form = HomeForm()
            messages.success(request, 'Your post was successfully created!')
            return redirect('broadcast:home')

        messages.warning(request, 'Please correct the error below.')  # <-
        context = {'form': form}
        return render(request, self.template_name, context)
