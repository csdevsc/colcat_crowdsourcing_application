from django.shortcuts import render, render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings

from manage.forms import *
from manage.models import *
from tasks.models import *

import os
import csv
from django.http import HttpResponse, HttpRequest

# Views
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if (username == settings.MANAGE_USERNAME and password == settings.MANAGE_PASS):
            return redirect('manage.views.main')
    return render(request, 'manage/login.html', {})

def main(request):
    # Make sure no direct access to main page
    try:
        referer = request.META['HTTP_REFERER']
    except:
        return redirect('manage.views.login')
    if referer.startswith('http://colcat.calit2.uci.edu:8003'):
        return render(request, 'manage/main.html', {})
    return redirect('manage.views.login')

# LANGUAGES
def new_language(request):
    if request.method == "POST":
        form = LanguageForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect(reverse('manage.views.view_languages'))
    else:
        form = LanguageForm()
    return render(request, 'manage/new-language.html', {'form': form})

def view_languages(request):
    language_list = Language.objects.all()
    context_dict = {'languages': language_list}
    return render(request, 'manage/view-languages.html', context_dict)

# IMAGES
def new_image(request):
    # Handle file upload
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            print request.FILES['image_filepath'].name
            print request.FILES['image_filepath']
            image_name = os.path.splitext(request.FILES['image_filepath'].name)[0]
            newimg = Image_Data(image_filepath = request.FILES['image_filepath'], image_id = image_name, language_name = request.POST.get('language_name'), task_type_id = request.POST.get('task_type_id'))
            newimg.save()
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('manage.views.view_images'))
    else:
        form = ImageForm() # A empty, unbound form
    return render(request, 'manage/new-image.html', {'form': form})

def view_images(request):
    image_list = Image_Data.objects.all()
    context_dict = {'images': image_list}
    return render(request, 'manage/view-images.html', context_dict)

# DATA MODELS
def new_data_model(request):
    if request.method == "POST":
        form = DataModelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect(reverse('manage.views.view_data_models'))
    else:
        form = DataModelForm()
    return render(request, 'manage/new-data-model.html', {'form': form})

def view_data_models(request):
    model_list = Data_Model.objects.all()
    context_dict = {'models': model_list}
    return render(request, 'manage/view-data-models.html', context_dict)

# TASKS
def new_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.language_id = request.POST.get('language_id')
            post.task_type_id = request.POST.get('task_type_id')
            post.image_id = request.POST.get('image_id')
            post.task_name = request.POST.get('language_id') + '_' + request.POST.get('task_type_id') + '_' + request.POST.get('image_id')
            post.task_url = '/tasks/'+request.POST.get('language_id')+'/'+request.POST.get('task_type_id') + '/'+request.POST.get('image_id')
            post.save()
            return HttpResponseRedirect(reverse('manage.views.view_tasks'))
    else:
        form = TaskForm()
    return render(request, 'manage/new-task.html', {'form': form})

def view_tasks(request):
    if request.method == "POST":
        if 'create_batch_file' in request.POST:
            print "Creating batch file..."
            task_choices = request.POST.getlist('task_choices')

            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="batch.csv"'
            writer = csv.writer(response)

            headers = ['task_language_id', 'task_type_id', 'task_img_id']
            writer.writerow(headers)
            for tid in task_choices:
                task = Task.objects.get(task_id=tid)
                task_info = [task.language_id, task.task_type_id, task.image_id]
                writer.writerow(task_info)
            print 'Finished writing batch file'

            return response
        elif 'mark_tasks_complete' in request.POST:
            print "Marking tasks complete..."
            tasks_complete = request.POST.getlist('tasks_complete')
            print tasks_complete
            for tid in tasks_complete:
                task = Task.objects.get(task_id=tid)
                task.complete = True
                task.save()
    task_list = Task.objects.all()
    context_dict = {'tasks': task_list}
    return render(request, 'manage/view-tasks.html', context_dict)

def new_task_type(request):
    if request.method == "POST":
        form = TaskTypeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect(reverse('manage.views.view_task_types'))
    else:
        form = TaskTypeForm()
    return render(request, 'manage/new-task-type.html', {'form': form})

def view_task_types(request):
    task_type_list = Task_Type.objects.all()
    context_dict = {'task_types': task_type_list}
    return render(request, 'manage/view-task-types.html', context_dict)

def new_task_template(request):
    if request.method == "POST":
        form = TaskTemplateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect(reverse('manage.views.view_task_templates'))
    else:
        form = TaskTemplateForm()
    return render(request, 'manage/new-task-template.html', {'form': form})

def view_task_templates(request):
    template_list = Task_Template.objects.all()
    context_dict = {'templates': template_list}
    return render(request, 'manage/view-task-templates.html', context_dict)

# RESPONSES
def download_responses(request):
    response_lists = []
    # Add objects for each response type
    try:
        response_list_foci_001 = Task_Foci_001.objects.all()
        response_lists.append(response_list_foci_001)
    except:
        pass
    try:
        response_list_naming_001 = Task_Naming_001.objects.all()
        response_lists.append(response_list_naming_001)
    except:
        pass

    context_dict = {'response_lists': [r.model.__name__ for r in response_lists]}
    for rlist in response_lists:
        write_responses_to_csv(rlist, 'uploads/responses/'+rlist.model.__name__+'.csv')
    return render(request, 'manage/download-responses.html', context_dict)

import csv
from django.db.models.loading import get_model

def write_responses_to_csv(qs, outfile_path):
    model = qs.model
    writer = csv.writer(open(outfile_path, 'w'))

    headers = []
    for field in model._meta.fields:
        headers.append(field.name)
    writer.writerow(headers)

    for obj in qs:
        row = []
        for field in headers:
            val = getattr(obj, field)
            if callable(val):
                val = val()
            if type(val) == unicode:
                val = val.encode("utf-8")
            row.append(val)
        writer.writerow(row)