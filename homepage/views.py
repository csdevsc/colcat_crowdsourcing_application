from django.shortcuts import render

# Views
def home(request):
    return render(request, 'homepage/home.html', {})

def login(request):
    return render(request, 'homepage/login.html', {})
