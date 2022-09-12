from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import gymlocation, trainer
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
import csv,re,json

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
    if request.POST['btlike'][0] == '좋':
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
    print(request.POST['inform']+'123')
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
            newgym = gymlocation(gym=gymname,location=i)
            newgym.save()
            j=1
            
    return render(request,'nuguhome/makegymlist.html')

def ConvertSystemSourcetoHtml(some):
    some = re.sub('\r\n','<br>',some)
    return some

"""    if '\r\n' in some:
        somelist = some.split('\r\n')
        resome = '<span>'
        for i in somelist:
            resome = resome + i +'<br></span><span>'
        resome +='</span>'"""
        
def backupdata(request):
    trainerlist = trainer.objects.all()
    trainerjson = []
    for i in trainerlist:
        trainerdic = {}
        trainerdic['gym'] = i.gym
        trainerdic['name'] = i.name
        trainerdic['like'] = i.like
        trainerdic['dislike'] = i.dislike
        trainerdic['mapurl'] = i.mapurl
        trainerdic['inform'] = i.inform
        trainerdic['created_at'] = i.created_at
        trainerjson.append(trainerdic)
    with open('.\\nuguhome\\static\data\\backuptrainer.json','w',encoding='utf-8') as tr_json:
        json.dump(trainerjson,tr_json,ensure_ascii=False,default=str,indent=2)
    return request
        
    
    