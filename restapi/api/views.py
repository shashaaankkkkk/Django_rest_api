from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import name
from .Serializers import namese
# Create your views here.

def hello(request):
    return HttpResponse("hello")
def api(request):
    
    names=name.objects.all()
    serial=namese(names,many=True)
    return JsonResponse(serial.data,safe=False)