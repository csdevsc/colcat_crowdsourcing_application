from django.shortcuts import render
from django.http import HttpResponse
from registration.backends.simple.views import RegistrationView
from crowdsource.models import Task, Response

def index(request):
    return render(request, 'crowdsource/index.html', {})

def about(request):
    return render(request, 'crowdsource/about.html', {})

class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return '/crowdsource/'

def task(request, task_name_slug):
    context_dict = {}

    try:
        task = Task.objects.get(slug=task_name_slug)
        context_dict['task_name'] = task.name
        context_dict['task'] = task
        context_dict['task_name_slug'] = task_name_slug
    except Task.DoesNotExist:
        pass

    return render(request, 'crowdsource/task.html', context_dict)
