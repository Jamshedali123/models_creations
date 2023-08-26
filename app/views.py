from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    tn=input('enter topic_name: ')
    to=topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    return HttpResponse('Data is inserted')
def insert_webpage(request):
    tn=input('enter topic_name: ')
    n=input('enter name: ')
    u=input('enter url: ')
    to=topic.objects.get(topic_name=tn)
    wo=webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    return HttpResponse('data inserted')
def insert_Ac(request):
    n=input('enter name: ')
    wo=webpage.objects.get(name=n)
    d=input('enter date: ')
    a=input('enter author: ')

  
    ao=accessRecord.objects.get_or_create(name=wo,date=d,author=a)[0]
    ao.save()
    return HttpResponse('data inserted')






def display_topics(request):
    QSTO=topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topics.html',d)


def display_webpages(request):
    QSWO=webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpages.html',d)


def display_access(request):
    QSAO=accessRecord.objects.all()
    d={'QSAO':QSAO}
    return render(request,'display_access.html',d)


def insert_topic(request):
    topic_name=input('enter topic_name')
    TO=topic.objects.get_or_create(topic_name=topic_name)[0]
    TO.save()
    QSTO=topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topics.html',d)



def insert_webpage(request):
    tn=input('enter topic_name')
    na=input('enter name')
    ur=input('enter url')

    TO=topic.objects.get(topic_name=tn)

    WO=webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
    WO.save()

    QSWO=webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpages.html',d)
































































