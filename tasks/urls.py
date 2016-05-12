"""colcat_crowdsourcing tasks URL Configuration
"""

from django.conf.urls import patterns, url
from tasks import views
from tasks.imports import *

urlpatterns = [
    url(r'^mturk-template/', views.mturk_template, name='mturk template'),
    url(r'^disclaimer/', views.disclaimer, name='disclaimer'),
    url(r'^prescreen/', views.prescreen, name='prescreen'),
    url(r'^practice-foci', views.practice_foci, {}),
    url(r'^(?P<language_id>\d+)/(?P<task_type_id>\d+)/(?P<img_id>\d+)$', views.get_task), # URL match for all tasks
]
