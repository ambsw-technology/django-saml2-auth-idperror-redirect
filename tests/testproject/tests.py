from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.test import TestCase


class IdpErrorRedirectTests(TestCase):

    def setUp(self) -> None:
        super().setUp()
        u = User.objects.create(
            username='test',
        )
        u.set_password('test')
        u.save()

    def test_error(self):
        """Without a proper setting, this plugin should result in an error"""
        with self.assertRaises(ValueError):
            self.client.get(
                '/test/',
            )

    def test_view(self):
        """Verify redirect to indicated view (with next)"""
        saml2_auth = dict(settings.SAML2_AUTH)
        saml2_auth['IDP_ERROR_REDIRECT_VIEW'] = 'login'
        with self.settings(SAML2_AUTH=saml2_auth):
            response = self.client.get(
                '/test/',
            )

        self.assertIsInstance(
            response,
            HttpResponseRedirect,
        )
        self.assertEqual(
            response.status_code,
            302,
        )
        self.assertEqual(
            '/login/',
            response.url,
        )

    def test_view_other(self):
        """The next parameters should only include the path even if we pass a full URL to get."""
        saml2_auth = dict(settings.SAML2_AUTH)
        saml2_auth['IDP_ERROR_REDIRECT_VIEW'] = 'other_login'
        with self.settings(SAML2_AUTH=saml2_auth):
            response = self.client.get(
                'http://testserver/test/',
            )

        self.assertIsInstance(
            response,
            HttpResponseRedirect,
        )
        self.assertEqual(
            response.status_code,
            302,
        )
        self.assertEqual(
            '/other_login/',
            response.url,
        )

    def test_next(self):
        """Verify redirect to indicated view (with next)"""
        saml2_auth = dict(settings.SAML2_AUTH)
        saml2_auth['IDP_ERROR_REDIRECT_VIEW'] = 'login'
        saml2_auth['IDP_ERROR_REDIRECT_NEXT'] = True
        with self.settings(SAML2_AUTH=saml2_auth):
            response = self.client.get(
                '/test/',
            )

        self.assertIsInstance(
            response,
            HttpResponseRedirect,
        )
        self.assertEqual(
            response.status_code,
            302,
        )
        self.assertEqual(
            '/login/?next=/test/',
            response.url,
        )

    def test_url(self):
        """The next parameters should only include the path even if we pass a full URL to get."""
        new_setting = dict(settings.SAML2_AUTH)
        new_setting['IDP_ERROR_REDIRECT_URL'] = 'http://example.com'
        with self.settings(SAML2_AUTH=new_setting):
            response = self.client.get(
                'http://testserver/test/',
            )

        self.assertIsInstance(
            response,
            HttpResponseRedirect,
        )
        self.assertEqual(
            response.status_code,
            302,
        )
        self.assertEqual(
            'http://example.com',
            response.url,
        )
