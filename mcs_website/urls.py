from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView
from crowdsource.views import MyRegistrationView

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/crowdsource/')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^crowdsource/', include('crowdsource.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)
