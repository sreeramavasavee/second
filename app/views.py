from django.shortcuts import render

from django.http import HttpResponse
def function1(request):
    return HttpResponse('<h1><marquee>this is my first project</h1></marquee>')

def function2(request):
    return HttpResponse('<h1><marquee>function 2</h1></marquee>')

