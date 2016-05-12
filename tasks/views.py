from django.shortcuts import render, render_to_response
from formtools.wizard.views import SessionWizardView
from tasks.models import Task_Foci_001
from django.utils.crypto import get_random_string
from tasks.imports import *
from manage.models import Task, Language
import random, traceback

# Helper functions
def generate_key():
    """Generate random key for each task"""
    unique_id = get_random_string(length=8)
    return unique_id

def get_task(request, language_id, task_type_id, img_id):
    x = request.GET.get('mtwid')
    random.seed(x)
    task_name = language_id + '_' + task_type_id + '_' + img_id
    print(task_name)
    # CHECK THAT TASK EXISTS
    if Task.objects.filter(task_name=task_name):
        try:
            inst_dict = {'language_id': language_id, 'task_type_id': task_type_id, 'img_id': img_id}
            return Foci_001_Wizard.as_view(sorted(Form_Task_Foci_001, key=lambda r:random.random()), instance_dict=inst_dict)(request)
        except:
            return render(request, 'error.html', {})
    else:
        print("Task Does Not Exist")
        return render(request, 'error.html', {})

class Foci_001_Wizard(SessionWizardView):
    template_name = 'tasks/foci-001.html'

    def dispatch(self, request, *args, **kwargs):
        self.w_id = request.GET.get('mtwid')
        #url(r'^(?P<language_id>\d+)/(?P<task_type_id>\d+)/(?P<img_id>\d+)$', views.get_task),
        self.language_id = self.instance_dict.get('language_id')
        self.language_name = Language.objects.get(language_id=self.language_id).language_name
        self.task_type_id = self.instance_dict.get('task_type_id')
        self.img_id = self.instance_dict.get('img_id')
        self.img_url = 'http://colcat.calit2.uci.edu:8003/uploads/data/' + self.language_name + '/' + self.task_type_id + '/' + self.img_id + '.png'
        return super(Foci_001_Wizard, self).dispatch(request, *args, **kwargs)

    def done(self, form_list, **kwargs):
        key = generate_key()
        instance = Task_Foci_001()
        setattr(instance, 'task_response_key', key)
        setattr(instance, 'worker_id', self.w_id)
        setattr(instance, 'task_img_id', self.img_id)
        setattr(instance, 'task_language_id', self.language_id)
        for form in form_list:
            for field, value in form.cleaned_data.iteritems():
                setattr(instance, field, value)
        instance.save()
        # save with key
        return render_to_response('tasks/completion.html', {'key': key})

# Views
def index(request):
    return render(request, 'tasks/index.html', {})

def mturk_template(request):
    return render(request, 'mturk_template.html', {})

def disclaimer(request):
    return render(request, 'tasks/disclaimer.html', {})

def prescreen(request):
    return render(request, 'tasks/prescreen.html', {})

def practice_foci(request):
    return render(request, 'practice_tasks/practice_foci.html', {})
