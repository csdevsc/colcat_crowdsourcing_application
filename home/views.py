from django.shortcuts import render

# Views
def index(request):
    return render(request, 'home/index.html', {})

def demo(request):
    return render(request, 'home/demo.html', {})

def about(request):
    return render(request, 'home/about.html', {})

def login(request):
    return render(request, 'home/login.html', {})
