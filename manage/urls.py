"""colcat_crowdsourcing tasks URL Configuration
"""

from django.conf.urls import patterns, url
from manage import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^main/$', views.main, name='main'),
    url(r'^new-language/$', views.new_language, name='new_language'),
    url(r'^view-languages/$', views.view_languages, name='view_languages'),
    url(r'^new-image/$', views.new_image, name='new_image'),
    url(r'^view-images/$', views.view_images, name='view_images'),
    url(r'^new-task/$', views.new_task, name='new_task'),
    url(r'^new-task-template/$', views.new_task_template, name='new_task_template'),
    url(r'^view-task-templates/$', views.view_task_templates, name='view_task_templates'),
    url(r'^view-tasks/$', views.view_tasks, name='view_tasks'),
    url(r'^new-task-type/$', views.new_task_type, name='new_task_type'),
    url(r'^view-task-types/$', views.view_task_types, name='view_tasks_types'),
    url(r'^new-data-model/$', views.new_data_model, name='new_data_model'),
    url(r'^view-data-models/$', views.view_data_models, name='view_data_models'),
    url(r'^download-responses/$', views.download_responses, name='download_responses'),
]
