import django_saml2_auth.views
from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    # Manually expose the SAML2 URLs so we can override the behavior for `denied`
    path('test/', views.test_view, name='test'),
    path('sso/', include('django_saml2_auth.urls', namespace='django_saml2_auth')),
    url(r'^other_login/$', django_saml2_auth.views.signin, name='other_login'),
    url(r'^login/$', django_saml2_auth.views.signin, name='login'),
]
