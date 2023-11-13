# created by self

from django.http import HttpResponse

def index(request):
    return  HttpResponse("Hello Jannu")
def about(request):
    return  HttpResponse('<h1 style="color:red;">About Section</h1>')

