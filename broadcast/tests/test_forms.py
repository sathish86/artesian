from django.test import TestCase
from broadcast.forms import HomeForm


class PostFormTests(TestCase):
    def test_post_forms__is_valid(self):
        """
        Test is_valid returns true for form validation
        :return:
        """
        form_data = {'post': 'Sample post data'}
        form = HomeForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_post_forms__is_not_valid(self):
        """
        Test is_valid return false for invalid input
        :return:
        """
        form_data = {'post': ''}
        form = HomeForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_post_forms__no_of_fields(self):
        """
        Test No.of fields form return
        :return:
        """
        form_data = {'post': 'ASDF'}
        form = HomeForm(data=form_data)
        self.assertEqual(len(form.fields), 1)
