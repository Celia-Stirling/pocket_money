from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Child

# Create your views here.

def index(request):
  children = Child.objects.all().values()
  template = loader.get_template('pocket_money.html')
  context = {
    'children': children,
  }
  return HttpResponse(template.render(context, request))