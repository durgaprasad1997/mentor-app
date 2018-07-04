from django.shortcuts import render
from onlineapp.models import Colleges
from onlineapp.models import Student
from onlineapp.models import Marks

# Create your views here.

from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views import View
from django.template import Context, loader


def get(request):
    #return "hello world"
    return HttpResponse('Hello, World!')

def index(request):
    c=open("C:/summer_apps/TTT.html","r")
    s=c.read()
    print(s)

    return HttpResponse(s)

def query(request):
    c=Colleges.objects.values('Name','Acronym')
    s=r"<html><body>"
    s+=r"<p>"
    for q in c:
        s+=(str(q)+"<br>")
    s+=r"</p></body></html>"


    return HttpResponse(s)

def query2(request):
    template = loader.get_template("C:/summer_apps/django_project/onlineproject/onlineapp/template/template1.html")
    c = Colleges.objects.values('Name', 'Acronym')
    dict={'data':c}

    return HttpResponse(template.render(dict,request))




def query3(request):
    template = loader.get_template("C:/summer_apps/django_project/onlineproject/onlineapp/template/template1.html")

    c = Student.objects.values('id', 'Name', 'Email_id', 'Colleges__Acronym').order_by('id')
    dict={'data':c}

    return HttpResponse(template.render(dict,request))

def query3_id(request,num):
    template = loader.get_template("C:/summer_apps/django_project/onlineproject/onlineapp/template/template1.html")

    c = Student.objects.filter(id=int(num)).values('id', 'Name', 'Email_id', 'Colleges__Acronym')
    dict={'data':c}

    return HttpResponse(template.render(dict,request))


def queryMarks(request):
    template = loader.get_template("C:/summer_apps/django_project/onlineproject/onlineapp/template/template2.html")

    c = Student.objects.values('id', 'Name', 'Email_id', 'Colleges__Acronym','marks__Total').order_by('id')
    dict={'data':c}

    return HttpResponse(template.render(dict,request))




def testSession(request):
    request.session.setdefault("counter",0)
    call=request.session["counter"]+1
    request.session["counter"]=call
    return HttpResponse(call)


def exceptiontest(request):
    raise Exception

