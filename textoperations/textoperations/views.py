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
    e = 0
    djtext = request.POST.get('prompt','default')
    data = djtext
    rpunc = request.POST.get('removepunc','off')
    if rpunc == 'on':
        e += 1
        result = ''
        punclist = '''"[]{\}/?.,:;'-+%&^*()_-=$#@!~”₹|`<>'''
        for i in djtext:
            if i not in punclist:
                result = result + i
        djtext = result

    extraspace = request.POST.get('extraspace','off')
    if extraspace == 'on':
        e += 1
        result = ''
        for i,item in enumerate(djtext):
            if item != ' ' and djtext[i+1] != ' ':
                result = result + item
                if i==len(djtext)-2:
                    if djtext[-1]!=' ':
                        result = result + djtext[-1]
                    break
        djtext = result

    removenewline = request.POST.get('removenewline','off')
    if removenewline == 'on':
        e += 1
        result = ''
        print(djtext)
        for i in djtext:
            if i != '\n' and i != '\r':
                result = result + i
        djtext = result

    text_format = request.POST.get('text-format','off')
    if text_format == 'capital':
        e += 1
        djtext = djtext.capitalize()

    elif text_format == 'lower':
        e += 1
        djtext = djtext.lower()

    elif text_format == 'upper':
        e += 1
        djtext = djtext.upper()

    elif text_format == 'title':
        e += 1
        djtext = djtext.title()

    if e:
        newtext = {'data':data,'result':djtext}
        return render(request, 'task.html', newtext)

    else:
        return HttpResponse("Please Select Task Punctuation")

