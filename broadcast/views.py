from django.shortcuts import render, redirect

from django.views.generic import TemplateView
from broadcast.forms import HomeForm
from broadcast.models import Post
from django.contrib import messages

from django.db.models import Q


class HomeView(TemplateView):
    # template view for both get and post operations
    template_name = 'broadcast/home.html'

    def get(self, request):
        """
        Used for rendering list of post and also used for search operation
        :param request: http request object
        :return: list of post objects
        """
        form = HomeForm()
        query = request.GET.get('q')
        if query:
            # multiple field search
            records = Post.objects.filter(Q(post__icontains=query) |
                                          Q(user__username__icontains=query) |
                                          Q(user__userprofile__role__icontains=query))
        else:
            records = Post.latest_post.all()

        return render(request, self.template_name, {'form': form, 'records': records})

    def post(self, request):
        """
        Creates post based on the input
        :param request: http request object
        :return: list of post objects
        """
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Your post was successfully created!')
            return redirect('broadcast:home')

        messages.warning(request, 'Please correct the error below.')  # <-
        context = {'form': form}
        return render(request, self.template_name, context)
