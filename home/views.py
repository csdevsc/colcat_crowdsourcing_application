from django.shortcuts import render
from manage.models import *
from home.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.utils.crypto import get_random_string

# Views
def index(request):
    return render(request, 'home/index.html', {})

def demo(request):
    return render(request, 'home/demo.html', {})

def about(request):
    return render(request, 'home/about.html', {})

def login(request):
    return render(request, 'home/login.html', {})

def home(request):
    user_id = get_random_string(length=10)
    if request.method == "POST":
        user_id = request.POST.get('user_id_input')
    task_list = Task.objects.filter(from_mturk=False).filter(complete=False)
    user_task_list = []
    for task in task_list:
        try:
            language = Language.objects.get(language_id=task.language_id).language_name
            tid = task.task_id
            timage = "/uploads/data/" + language + "/" + task.task_type_id + "/" + task.image_id + ".png"
            task_params = task.task_url.split('/')
            task_language_id = task_params[2]
            task_type_id = task_params[3]
            task_img_id = task_params[4]
            tlink = '/tasks/disclaimer?mtwid=' + user_id + '&tlid=' + task_language_id + '&ttid=' + task_type_id + '&tiid=' + task_img_id
            utask = UserTask(tid, timage, tlink) #Task.objects.get(task_id=tid)
            user_task_list.append(utask)
        except ObjectDoesNotExist:
            print 'Failed to fetch something'
    print user_task_list
    context_dict = {'tasks': user_task_list, 'user_id': user_id}
    return render(request, 'home/home.html', context_dict)
