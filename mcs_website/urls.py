from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView
from crowdsourcing.views import MyRegistrationView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/crowdsourcing/')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^crowdsourcing/', include('crowdsourcing.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)
