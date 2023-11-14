from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import name
from .Serializers import namese
# Create your views here.

def hello(request):
    return HttpResponse("hello")
def api(request):
    data1=name.objects.all()
    serial=namese(data1,many=True)
    return JsonResponse(serial.data,safe=False)