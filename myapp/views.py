from django.shortcuts import render
from rest_framework.decorators import api_view
from myapp.models import Users

# Create your views here.
@api_view(['GET', 'POST'])
def login(request):
    request.GET.get('name')
    return render(request, 'login.html', {})

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})