from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import gymlocation, trainer
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
import csv,re

# Create your views here.


def home(request):
    latest_trainer_list = trainer.objects.all()
    template = loader.get_template('nuguhome/homepage.html')
    context = {
        'latest_trainer_list': latest_trainer_list,
    }
    return HttpResponse(template.render(context,request))

def write(request):
    latest_gym_list = gymlocation.objects.all()
    template = loader.get_template('nuguhome/write.html')
    context = {
        'latest_gym_list': latest_gym_list,
    }   
    return HttpResponse(template.render(context,request))

@csrf_exempt
def like(request):
    trainerone = trainer.objects.get(id=request.POST['hiddenlike'])
    if request.POST['btlike'] == '좋아요':
        trainerone.like +=1
        trainerone.save()
    else:
        trainerone.dislike+=1
        trainerone.save()
    latest_trainer_list = trainer.objects.all()
    template = loader.get_template('nuguhome/homepage.html')
    context = {
        'latest_trainer_list': latest_trainer_list,
    }
    return HttpResponse(template.render(context,request))

@csrf_exempt
def wrote(request):
    map = 'https://map.naver.com/v5/search/'+str(gymlocation.objects.get(gym=request.POST['gym']).location)
    print(ConvertSystemSourcetoHtml(request.POST['inform']))
    newtrainer = trainer(gym = request.POST['gym'],
                         name = request.POST['name'],
                         inform= ConvertSystemSourcetoHtml(request.POST['inform']),
                         mapurl = map)
    newtrainer.save()
    latest_trainer_list = trainer.objects.all()
    template = loader.get_template('nuguhome/homepage.html')
    context = {
        'latest_trainer_list': latest_trainer_list,
    }
    return HttpResponse(template.render(context,request))


def makegymlist(request):
    return render(request,'nuguhome/makegymlist.html')

@csrf_exempt
def makegymlist2(request):
    gym_json = str(request.POST['json'])
    gymforjson = gym_json.split('*')
    j=1
    for i in gymforjson:
        if len(i)<1:
            continue
        if j%2==1:
            gymname = i
            j +=1
        else:
            print(gymname)
            print(i)
            newgym = gymlocation(gym=gymname,location=i)
            newgym.save()
            j=1
            
    return render(request,'nuguhome/makegymlist.html')

def ConvertSystemSourcetoHtml(some):
    some = re.sub('\"',"&quot;",some)
    some = re.sub('\'',"&#39;",some)
    some = re.sub('\n'," ",some)
    some = re.sub('\r'," ",some)
    return some
