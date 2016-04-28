from django.shortcuts import render, render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from manage.forms import *
from manage.models import *
from tasks.models import *

# Views
def index(request):
    return render(request, 'manage/index.html', {})

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
            newimg = Image_Data(image_filepath = request.FILES['image_filepath'], language_name = request.POST.get('language_name'), task_type_name = request.POST.get('task_type_name'))
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

# TASKS
def new_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.task_name = request.POST.get('language_name') + '_' + request.POST.get('task_type_name') + '_' + request.POST.get('image_filepath')
            post.task_url = '/tasks/'+request.POST.get('language_name')+'/'+request.POST.get('task_type_name') + '/'+request.POST.get('image_filepath')
            post.save()
            return HttpResponseRedirect(reverse('manage.views.view_tasks'))
    else:
        form = TaskForm()
    return render(request, 'manage/new-task.html', {'form': form})

def view_tasks(request):
    if request.method == "GET":
        task_list = Task.objects.all()
        context_dict = {'tasks': task_list}
        return render(request, 'manage/view-tasks.html', context_dict)
    else:
        return HttpResponseRedirect(reverse('manage.views.view_tasks'))

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

# RESPONSES
def download_responses(request):
    response_list = Task_Foci_001.objects.all()
    context_dict = {'responses': response_list}
    dump(response_list, 'uploads/responses/output.csv')
    return render(request, 'manage/download-responses.html', context_dict)

import csv
from django.db.models.loading import get_model

def dump(qs, outfile_path):
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
