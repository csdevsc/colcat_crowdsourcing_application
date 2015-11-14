from django.shortcuts import render, render_to_response
from formtools.wizard.views import SessionWizardView
from tasks.models import Task_Naming_001, Task_Foci_001, Task_Mapping_001
from django.utils.crypto import get_random_string
from tasks.imports import *
import random

# Helper functions
def generate_key():
    """Generate random key for each task"""
    unique_id = get_random_string(length=8)
    return unique_id

def get_form_list(request, task):
    x = request.GET.get('mtwid')
    random.seed(x)
    if task == 'foci-001':
        return Foci_001_Wizard.as_view(sorted(Form_Task_Foci_001, key=lambda r:random.random()))(request)
    elif task == 'foci-002':
        return Foci_002_Wizard.as_view(sorted(Form_Task_Foci_001, key=lambda r:random.random()))(request)
    elif task == 'foci-003':
        return Foci_003_Wizard.as_view(sorted(Form_Task_Foci_001, key=lambda r:random.random()))(request)
    elif task == 'naming':
        return Naming_001_Wizard.as_view(sorted(Form_Task_Naming_001, key=lambda r:random.random()))(request)
    elif task == 'mapping':
        return Mapping_001_Wizard.as_view(sorted(Form_Task_Mapping_001, key=lambda r:random.random()))(request)
    else:
        return render(request, 'error.html', {})

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

class Naming_001_Wizard(SessionWizardView):
    template_name = 'tasks/naming.html'

    def dispatch(self, request, *args, **kwargs):
        self.w_id = request.GET.get('mtwid')
        return super(Naming_001_Wizard, self).dispatch(request, *args, **kwargs)

    def done(self, form_list, **kwargs):
        key = generate_key()
        instance = Task_Naming_001()
        setattr(instance, 'task_response_key', key)
        setattr(instance, 'worker_id', self.w_id)
        for form in form_list:
            for field, value in form.cleaned_data.iteritems():
                setattr(instance, field, value)
        instance.save()
        # save with key
        return render_to_response('tasks/completion.html', {'key': key})

class Foci_001_Wizard(SessionWizardView):
    template_name = 'tasks/foci-001.html'

    def dispatch(self, request, *args, **kwargs):
        self.w_id = request.GET.get('mtwid')
        return super(Foci_001_Wizard, self).dispatch(request, *args, **kwargs)

    def done(self, form_list, **kwargs):
        key = generate_key()
        instance = Task_Foci_001()
        setattr(instance, 'task_response_key', key)
        setattr(instance, 'worker_id', self.w_id)
        for form in form_list:
            for field, value in form.cleaned_data.iteritems():
                setattr(instance, field, value)
        instance.save()
        # save with key
        return render_to_response('tasks/completion.html', {'key': key})

class Foci_002_Wizard(SessionWizardView):
    template_name = 'tasks/foci-002.html'

    def dispatch(self, request, *args, **kwargs):
        self.w_id = request.GET.get('mtwid')
        return super(Foci_002_Wizard, self).dispatch(request, *args, **kwargs)

    def done(self, form_list, **kwargs):
        key = generate_key()
        instance = Task_Foci_001()
        setattr(instance, 'task_response_key', key)
        setattr(instance, 'worker_id', self.w_id)
        for form in form_list:
            for field, value in form.cleaned_data.iteritems():
                setattr(instance, field, value)
        instance.save()
        # save with key
        return render_to_response('tasks/completion.html', {'key': key})

class Foci_003_Wizard(SessionWizardView):
    template_name = 'tasks/foci-003.html'

    def dispatch(self, request, *args, **kwargs):
        self.w_id = request.GET.get('mtwid')
        return super(Foci_003_Wizard, self).dispatch(request, *args, **kwargs)

    def done(self, form_list, **kwargs):
        key = generate_key()
        instance = Task_Foci_001()
        setattr(instance, 'task_response_key', key)
        setattr(instance, 'worker_id', self.w_id)
        for form in form_list:
            for field, value in form.cleaned_data.iteritems():
                setattr(instance, field, value)
        instance.save()
        # save with key
        return render_to_response('tasks/completion.html', {'key': key})

class Mapping_001_Wizard(SessionWizardView):
    template_name = 'tasks/mapping.html'

    def dispatch(self, request, *args, **kwargs):
        self.w_id = request.GET.get('mtwid')
        return super(Mapping_001_Wizard, self).dispatch(request, *args, **kwargs)

    def done(self, form_list, **kwargs):
        key = generate_key()
        instance = Task_Mapping_001()
        setattr(instance, 'task_response_key', key)
        setattr(instance, 'worker_id', self.w_id)
        for form in form_list:
            for field, value in form.cleaned_data.iteritems():
                setattr(instance, field, value)
        instance.save()
        # save with key
        return render(request, 'tasks/completion.html', {'key': key})
