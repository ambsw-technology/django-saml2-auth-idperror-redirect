from django_saml2_auth.views import _idp_error


def test_view(request):
    return _idp_error(request, 'test error')
