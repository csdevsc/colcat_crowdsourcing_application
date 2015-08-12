from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'tasks/index.html', {})

def mturk_template(request):
    return render(request, 'mturk_template.html', {})
