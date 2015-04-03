from django.shortcuts import render
from django.http import HttpResponse
from registration.backends.simple.views import RegistrationView
from crowdsourcing.models import Task
from crowdsourcing.forms import Task_OCRTranscription, Task_OCRVerification, Task_CrowdsourceVerification
from crowdsourcing.forms import Task_NamingTranscription1, Task_NamingTranscription2

def index(request):
    return render(request, 'crowdsourcing/index.html', {})

def about(request):
    return render(request, 'crowdsourcing/about.html', {})

class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return '/crowdsourcing/'

def task(request, task_name_slug):
    context_dict = {}

    try:
        task = Task.objects.get(slug=task_name_slug)
        context_dict['task_name'] = task.name
        context_dict['task'] = task
        context_dict['task_name_slug'] = task_name_slug

        print(task.task_id)
        if request.method == 'POST':
            if (task.task_id == 1):
                form = Task_OCRVerification(request.POST)
            elif (task.task_id == 2):
                form = Task_OCRTranscription(request.POST)
            elif (task.task_id == 3):
                form = Task_CrowdsourceVerification(request.POST)
            elif (task.task_id == 4):
                form = Task_NamingTranscription1(request.POST)
            elif (task.task_id == 5):
                form = Task_NamingTranscription2(request.POST)

            if form.is_valid():
                form.save(commit=True)
                return index(request)
            else:
                print(form.errors)
        else:
            if (task.task_id == 1):
                form = Task_OCRVerification()
            elif (task.task_id == 2):
                form = Task_OCRTranscription()
            elif (task.task_id == 3):
                form = Task_CrowdsourceVerification()
            elif (task.task_id == 4):
                form = Task_NamingTranscription1()
            elif (task.task_id == 5):
                form = Task_NamingTranscription2()

        context_dict['form'] = form

    except Task.DoesNotExist:
        pass

    return render(request, 'crowdsourcing/task.html', context_dict)

# # OCR Verification Task
# @login_required
# def Task_NamingRanges1Form(request):
#     if request.method == 'POST'
#         form = Task_NamingRanges1Form(request.POST)
#
#         if form.is_valid():
#             form.save(commit=True)
#             return index(request)
#         else:
#             print(form.errors)
#     else:
#         form = TaskNamingRanges1Form()
#
#     return render(request, 'rango/', {'form': form})
