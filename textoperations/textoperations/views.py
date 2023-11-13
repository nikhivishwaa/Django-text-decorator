# created by self

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {"name":"Nikhil","message":"Happy Birthday Bro"}
    return  render(request, 'index.html', params)
    # return  render(request, 'index.html')

    # return  HttpResponse("Hello Jannu")

def about(request):
    return  HttpResponse('<h1 style="color:red;">About Section</h1>')

def services(request):
    return HttpResponse("Services page")

def relation(request):
    return HttpResponse("Relation page")

def task(request):
    # get the text
    djtext = request.GET.get('prompt','default')
    rpunc = request.GET.get('removepunc','off')
    if rpunc == 'on':
        result = ''
        punclist = '''"[]{\}/?.,:;'-+%&^*()_-=$#@!~`<>'''
        for i in djtext:
            if i not in punclist:
                result = result + i
        newtext = {'task':'Remove Punctuation','result':result}
        return render(request, "task.html", newtext)

    return HttpResponse("Please Select Task Punctuation")

