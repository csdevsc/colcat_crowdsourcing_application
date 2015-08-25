from django.shortcuts import render, render_to_response
from formtools.wizard.views import SessionWizardView
from tasks.models import Task_Naming_001, Task_Foci_001, Task_Mapping_001
from django.utils.crypto import get_random_string

# Helper functions.
def generate_key():
    """Generate random key for each task"""
    unique_id = get_random_string(length=8)
    return unique_id

# Create your views here.
def index(request):
    return render(request, 'tasks/index.html', {})

def mturk_template(request):
    return render(request, 'mturk_template.html', {})

def prescreen(request):
    return render(request, 'tasks/prescreen.html', {})

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
    template_name = 'tasks/foci.html'

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

class Mapping_001_Wizard(SessionWizardView):
    template_name = 'tasks/mapping.html'

    def dispatch(self, request, *args, **kwargs):
        self.w_id = request.GET.get('mtwid')
        return super(Mapping_001_Wizard, self).dispatch(request, *args, **kwargs)

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
