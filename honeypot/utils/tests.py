from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse


class CSRFTests(TestCase):
    """
    Test cases for establishing the relative security settings for Django's
    CSRF Middleware.

    """
    fixtures = ['test-data.json']

    def test_csrf(self):
        """
        Instantiate a CSRF-aware test client and verify that the CSRF
        Middleware is working in the most basic functionality.

        """

        csrf_client = Client(enforce_csrf_checks=True)
        csrf_client.login(username='archen', password='mytestpassword')

        # todo: add settings for test URL
        response = csrf_client.get(reverse('hackme:vote', kwargs={'question_id': 1}))

        csrf_token = "{0}".format(response.context['csrf_token'])  # get the token

        post_data = {
            'csrfmiddlewaretoken': csrf_token,
            'choice': 1,
        }

        # todo: add settings for test URL
        response = csrf_client.post(reverse('hackme:vote', kwargs={'question_id': 1}),
                                    post_data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_csrf_token_session_rotation(self):
        """
        Instantiate a CSRF-aware test client and verify that the CSRF
        Middleware rotates the CSRF token per session by logging in
        getting token1, logging out and back in, getting token2, then
        assert that token1 does not equal token2.

        """

        csrf_client = Client(enforce_csrf_checks=True)
        csrf_client.login(username='archen', password='mytestpassword')

        # todo: add settings for test URL
        response = csrf_client.get(reverse('hackme:vote', kwargs={'question_id': 1}))
        token1 = "{0}".format(response.context['csrf_token'])

        csrf_client.logout()
        csrf_client.login(username='archen', password='mytestpassword')

        # todo: add settings for test URL
        response = csrf_client.get(reverse('hackme:vote', kwargs={'question_id': 1}))
        token2 = "{0}".format(response.context['csrf_token'])

        self.assertNotEqual(token1, token2, msg='CSRF Token is not rotated per session')

    def test_csrf_token_request_rotation(self):
        """
        Instantiate a CSRF-aware test client and verify that the CSRF
        Middleware rotates the CSRF token per request by logging in
        getting token1, getting token2, then assert that token1 does
        not equal token2.

        """

        csrf_client = Client(enforce_csrf_checks=True)
        csrf_client.login(username='archen', password='mytestpassword')

        # todo: add settings for test URL
        response = csrf_client.get(reverse('hackme:vote', kwargs={'question_id': 1}))
        token1 = "{0}".format(response.context['csrf_token'])

        # todo: add settings for test URL
        response = csrf_client.get(reverse('hackme:vote', kwargs={'question_id': 1}))
        token2 = "{0}".format(response.context['csrf_token'])

        self.assertNotEqual(token1, token2, msg='CSRF Token is not rotated per request')