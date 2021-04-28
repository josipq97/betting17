from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    matches = Matches.objects.all()
    return render(request, 'index.html', {'matches': matches})
