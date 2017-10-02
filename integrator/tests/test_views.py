# Create your tests here.
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import RequestFactory
from django.contrib.auth.models import User
from django.test import Client
from integrator import views

from django.contrib.messages.storage.fallback import FallbackStorage
# below import works only with python 3.4 or greater
from unittest.mock import patch, MagicMock

from integrator.models import Corporate


class PostViewsTestCase(TestCase):
    fixtures = ['broadcast_user_testdata.json', 'integrator_userprofile_testdata.json',
                'integrator_investor_testdata.json', 'integrator_startup_testdata.json',
                'integrator_corporate_testdata.json']

    def setUp(self):
        self.user = User.objects.first()
        self.factory = RequestFactory()
        self.client = Client()

    def test_view_profile__expect_profile_information(self):
        """
        Test to return profile information of user
        :return: None
        """
        request = self.factory.get(reverse('integrator:view_profile'))
        request.user = self.user
        response = views.view_profile(request)
        self.assertContains(response, 'sathish.cres07@gmail.com', count=1, status_code=200)

    def test_view_profile__pass_pk(self):
        """
        Test to return profile information of another user using primary key
        :return: None
        """
        request = self.factory.get(reverse('integrator:view_profile'))
        request.user = self.user
        another_user = User.objects.last()
        response = views.view_profile(request, pk=another_user.pk)
        self.assertContains(response, 'suncorp@gmail.com', count=1, status_code=200)

    def test_get_collaborator__should_return_all_collaborators(self):
        """
        Test to return profile information of another user using primary key
        :return: None
        """
        request = self.factory.get(reverse('integrator:view_profile'))
        request.user = User.objects.get(pk=10)
        response = views.get_collaborator(request)
        self.assertEqual(2, len(response))
        expected_username = ['startup', 'nrma']
        response_list_username = []
        for rec in response:
            response_list_username.append(rec.username)

        self.assertEquals(expected_username.sort(), response_list_username.sort())

    def test_list_collaborators__test_mapped_collaborators(self):
        """
        Test to return list of available users and current user mapped list
        :return: None
        """
        request = self.factory.get(reverse('integrator:view_profile'))
        request.user = User.objects.get(pk=10)
        response = views.list_collaborators(request)
        expected_username = ['startup', 'nrma']
        self.assertContains(response, expected_username[0], count=4, status_code=200)
        self.assertContains(response, expected_username[1], count=2, status_code=200)

    def test_change_collaboration__add_new_collaborator(self):
        """
        Test to add new collaborator to current user.
        :return: None
        """
        import pdb; pdb.set_trace()
        request = self.factory.get(reverse('integrator:view_profile'))
        request.user = User.objects.get(pk=10)
        no_of_collaborators = Corporate.objects.get(current_user=request.user)
        self.assertEquals(2, len(no_of_collaborators.users.all()))
        new_user_pk = User.objects.get(pk=11).pk
        # method call to add existing user
        views.change_collaboration(request, operation="add", pk=new_user_pk)
        # check it added this new user
        no_of_collaborators = Corporate.objects.get(current_user=request.user)
        self.assertEquals(3, len(no_of_collaborators.users.all()))

    def test_change_collaboration__remove_new_collaborator(self):
        """
        Test to add new collaborator to current user.
        :return: None
        """
        request = self.factory.get(reverse('integrator:view_profile'))
        request.user = User.objects.get(pk=10)
        no_of_collaborators = Corporate.objects.get(current_user=request.user)
        self.assertEquals(2, len(no_of_collaborators.users.all()))

        existing_user_pk = User.objects.get(pk=12).pk
        # method call to remove existing user
        views.change_collaboration(request, operation="remove", pk=existing_user_pk)
        # check it added this new user
        no_of_collaborators = Corporate.objects.get(current_user=request.user)
        self.assertEquals(1, len(no_of_collaborators.users.all()))
