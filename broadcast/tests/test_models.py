# Create your tests here.
from django.test import TestCase

from broadcast.models import Post


class PostModelTestCase(TestCase):
    fixtures = ['broadcast_user_testdata.json', 'integrator_userprofile_testdata',
                'broadcast_views_testdata.json']

    def test_post_model__count(self):
        """
        Test Post object returns correct count
        :return:
        """
        post_objects = Post.objects.all()
        self.assertEqual(13, post_objects.count())
