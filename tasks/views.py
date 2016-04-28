from django.shortcuts import render, render_to_response
from formtools.wizard.views import SessionWizardView
from tasks.models import Task_Naming_001, Task_Foci_001, Task_Mapping_001, Document
from django.utils.crypto import get_random_string
from tasks.imports import *
from manage.models import Task
import random

# Helper functions
def generate_key():
    """Generate random key for each task"""
    unique_id = get_random_string(length=8)
    return unique_id

# from django.template import RequestContext
# from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse
#
# def list(request):
#     # Handle file upload
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             newdoc = Document(docfile = request.FILES['docfile'])
#             newdoc.save()
#
#             # Redirect to the document list after POST
#             return HttpResponseRedirect(reverse('tasks.views.list'))
#     else:
#         form = DocumentForm() # A empty, unbound form
#
#     # Load documents for the list page
#     documents = Document.objects.all()
#
#     # Render list page with the documents and the form
#     return render_to_response(
#         'tasks/list.html',
#         {'documents': documents, 'form': form},
#         context_instance=RequestContext(request)
#     )
#
# def index(request):
#     return render_to_response('myapp/index.html')

def get_form_list(request, task):
    x = request.GET.get('mtwid')
    random.seed(x)
    if task == 'foci-001':
        return Foci_001_Wizard.as_view(sorted(Form_Task_Foci_001, key=lambda r:random.random()))(request)
    elif task == 'foci-002':
        return Foci_002_Wizard.as_view(sorted(Form_Task_Foci_001, key=lambda r:random.random()))(request)
    elif task == 'foci-003':
        return Foci_003_Wizard.as_view(sorted(Form_Task_Foci_001, key=lambda r:random.random()))(request)
    elif task == 'foci-004':
        return Foci_004_Wizard.as_view(sorted(Form_Task_Foci_001, key=lambda r:random.random()))(request)
    elif task == 'naming':
        return Naming_001_Wizard.as_view(sorted(Form_Task_Naming_001, key=lambda r:random.random()))(request)
    elif task == 'mapping':
        return Mapping_001_Wizard.as_view(sorted(Form_Task_Mapping_001, key=lambda r:random.random()))(request)
    else:
        return render(request, 'error.html', {})

def get_task(request, language_id, task_type_id, img_id):
    x = request.GET.get('mtwid')
    random.seed(x)
    task_name = language_id + '_' + task_type_id + '_1' #TODO: + img_id[-1]
    print(task_name)
    # CHECK THAT TASK EXISTS
    if Task.objects.filter(task_name=task_name):
        try:
            inst_dict = {'language_id': language_id, 'task_type_id': task_type_id, 'img_id': img_id}
            return Foci_001_New_Wizard.as_view(sorted(Form_Task_Foci_001, key=lambda r:random.random()), instance_dict=inst_dict)(request)
        except:
            return render(request, 'error.html', {})
    else:
        return render(request, 'error.html', {})

class Foci_001_New_Wizard(SessionWizardView):
    template_name = 'tasks/foci-001.html'

    def dispatch(self, request, *args, **kwargs):
        self.w_id = request.GET.get('mtwid')
        #url(r'^(?P<language_id>\d+)/(?P<task_type_id>\d+)/(?P<img_id>\d+)$', views.get_task),
        self.language_id = self.instance_dict.get('language_id')
        self.task_type_id = self.instance_dict.get('task_type_id')
        self.img_id = self.instance_dict.get('img_id')
        self.img_url = 'http://localhost:8000/uploads/data/' + self.language_id + '/' + self.task_type_id + '/' + self.img_id + '.png'
        return super(Foci_001_New_Wizard, self).dispatch(request, *args, **kwargs)

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
        setattr(instance, 'task_img_id', '001')
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
        setattr(instance, 'task_img_id', '002')
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
        setattr(instance, 'task_img_id', '003')
        for form in form_list:
            for field, value in form.cleaned_data.iteritems():
                setattr(instance, field, value)
        instance.save()
        # save with key
        return render_to_response('tasks/completion.html', {'key': key})

class Foci_004_Wizard(SessionWizardView):
    template_name = 'tasks/foci-004.html'

    def dispatch(self, request, *args, **kwargs):
        self.w_id = request.GET.get('mtwid')
        self.ti_id = request.GET.get('tiid')
        return super(Foci_004_Wizard, self).dispatch(request, *args, **kwargs)

    def done(self, form_list, **kwargs):
        key = generate_key()
        instance = Task_Foci_001()
        setattr(instance, 'task_response_key', key)
        setattr(instance, 'worker_id', self.w_id)
        setattr(instance, 'task_img_id', '004')
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
