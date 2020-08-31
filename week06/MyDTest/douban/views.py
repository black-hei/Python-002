from django.shortcuts import render
from django.http import HttpResponse
from .models import Film

# Create your views here.

def films(request):

   n = Film.objects.all()

   return render (request, 'index.html', locals())