"""colcat_crowdsourcing tasks URL Configuration
"""

from django.conf.urls import patterns, url
from tasks import views
from tasks.views import Naming_001_Wizard, Foci_001_Wizard, Mapping_001_Wizard
from tasks.imports import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mturk-template/', views.mturk_template, name='mturk template'),
    url(r'^disclaimer/', views.disclaimer, name='disclaimer'),
    url(r'^prescreen/', views.prescreen, name='prescreen'),
    url(r'^foci/001', views.get_form_list, {'task' : 'foci-001'}),
    url(r'^foci/002', views.get_form_list, {'task' : 'foci-002'}),
    url(r'^foci/003', views.get_form_list, {'task' : 'foci-003'}),
    url(r'^practice-foci', views.practice_foci, {}),
    url(r'^naming/001', views.get_form_list, {'task': 'naming'}),
    url(r'^mapping/001', views.get_form_list, {'task' : 'mapping'}),
]
