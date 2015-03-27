from django.shortcuts import render
from django.http import HttpResponse
from registration.backends.simple.views import RegistrationView

def index(request):
    return render(request, 'crowdsource/index.html', {})

def about(request):
    return render(request, 'crowdsource/about.html', {})

class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return '/crowdsource/'
