"""colcat_crowdsourcing tasks URL Configuration
"""

from django.conf.urls import patterns, url
from tasks import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mturk-template/', views.mturk_template, name='mturk template'),
]
