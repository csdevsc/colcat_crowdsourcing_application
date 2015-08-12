"""colcat_crowdsourcing tasks URL Configuration
"""

from django.conf.urls import patterns, url
from tasks import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
