from django.conf.urls import url
from broadcast.views import HomeView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
]
