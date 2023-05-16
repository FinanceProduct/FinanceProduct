from django.shortcuts import render
from django.conf import settings

# Create your views here.
def home(request):
    context = {

    }
    return render(request, 'home/home.html', context)