from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.contrib import messages
from Accounts.models import profile,classroom
from Accounts.forms import Classform
from django.contrib.auth.decorators import login_required
from Accounts.decarators import is_class_member,is_class_admin
from Accounts.randgenrator import rand
# Create your views here.
@login_required
def createclass(request):
    if request.POST:
        form=Classform(request.POST)
        if (form.is_valid()):
            #form.save()
            classname=request.POST['class_name']
            class_sub=request.POST['class_subject']
            class_section=request.POST['class_sec']
            cid=rand(6)
            url='classroom/'+cid
            c=classroom(class_name=classname,class_sec=class_section,class_subject=class_sub,classid=cid,admin=request.user,c_url=url)
            c.save()
            c.members.add(request.user.profile)
        return redirect(url)

    else:
        form=Classform(request.POST)
    return render(request,'home.html',{'form':form})
@login_required
def joinclass(request):
    if request.POST:
        c_id=request.POST['classid']
        try:
            join_class=classroom.objects.get(classid=c_id)
        except classroom.DoesNotExist:
            messages.error(request,f'No Class Exists')
            return redirect('/classroom')
        user=profile.objects.get(user=request.user)
        join_class.members.add(user)
        return redirect('classroom/'+c_id)

def home(request):
    form=Classform(request.POST)
    #user=profile.objects.get(user=request.user)
    #user=profile.objects.all()
    #loc=TEMP
    return render(request,'home.html',{'tittle':'home','form':form})
    #return HttpResponse("<h1>HELLO WORLD</h1>")

def some(request,idk):
    try:
        a=profile.objects.get(user_id=idk)
    except profile.DoesNotExist:
        raise Http404('USER NOT FOUND')
    return render(request,'help.html',{'a':a})
    #return HttpResponse("<h1><a href="">hi</a></h1>")

def catalogue(request):
    form=Classform(request.POST)
    return render(request,'catalogue.html',{'form':form,'tittle':'catalogue'})

def help(request):
    form=Classform(request.POST)
    return render(request,'help.html',{'form':form,'tittle':'help'})

@login_required
def class_room(request):
    form=Classform(request.POST)
    userclass=classroom.objects.filter(members=request.user.profile)
    return render(request,'classroom_home.html',{'form':form,'user_classes':userclass})

@login_required
@is_class_member(allowed_class=[])
def CLASSROOM(request,c_id):
    form=Classform(request.POST)
    return HttpResponse("<h1>hi</h1>")

@is_class_admin
def classadmin(request,c_id):
    return HttpResponse("<h1>hi Admin</h1>")