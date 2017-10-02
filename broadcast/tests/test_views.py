# Create your tests here.
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import RequestFactory
from django.contrib.auth.models import User
from broadcast.views import HomeView
from broadcast.models import Post
from django.contrib.messages.storage.fallback import FallbackStorage
# below import works only with python 3.4 or greater
from unittest.mock import patch, MagicMock


class PostViewsTestCase(TestCase):
    fixtures = ['broadcast_user_testdata.json', 'integrator_userprofile_testdata', 'broadcast_views_testdata.json']

    def setUp(self):
        self.user = User.objects.first()
        self.factory = RequestFactory()

    def test_post_list__check_it_redirects_login(self):
        """
        Check it redirects to login url
        :return: None
        """

        resp = self.client.get(reverse('broadcast:home'))
        self.assertEqual(resp.status_code, 302)
        self.assertTrue('/integrator/login/' in resp.url)

    def test_post__get_expected_response(self):
        """
        Test it return list of post objects
        :return:
        """
        request = self.factory.get(reverse('broadcast:home'))
        request.user = self.user
        response = HomeView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        for rec in Post.objects.all():
            self.assertContains(response, rec.post, status_code=200)

    @patch('broadcast.models.Post.save', MagicMock(name="save"))
    def test_post__post_calls_save_method(self):
        """
        Test post requests
        """
        # Create the request
        data = {
            'post': 'My snippet'
        }

        request = self.factory.post(reverse('broadcast:home'), data)
        # we need to set these attributes for message middleware to work with factory class.
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        request.user = self.user
        # Get the response
        response = HomeView.as_view()(request)
        self.assertEqual(response.status_code, 302)
        # Check save was called
        self.assertTrue(Post.save.called)
        self.assertEqual(Post.save.call_count, 1)

    def test_post__search_response(self):
        """
        Test search result as expected value
        :return:
        """
        request = self.factory.get(reverse('broadcast:home'), data={'q': 'Investor campaign'})
        request.user = self.user
        response = HomeView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Investor campaign', count=2, status_code=200)

    def test_post__no_search_result(self):
        """
        Test search result should not return result
        :return:
        """
        request = self.factory.get(reverse('broadcast:home'), data={'q': 'Test post 1'})
        request.user = self.user
        response = HomeView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test post', count=1, status_code=200)
