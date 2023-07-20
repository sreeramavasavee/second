from django.shortcuts import render
from django.http import HttpResponse
def startproject(request):
    return HttpResponse('<marquee> this is my 2 function </marquee>')
def startproject2(request):
    return HttpResponse('2nd app')