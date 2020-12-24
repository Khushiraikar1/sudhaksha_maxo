from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.contrib import messages
from Accounts.models import profile,classroom,timetable
from Accounts.forms import Classform,timetableform
from django.contrib.auth.decorators import login_required
from Accounts.decarators import is_class_member,is_class_admin
from Accounts.randgenrator import rand
# Create your views here.
week=['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY']
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
    form=Classform()
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
def formtimetable(contents):
    context=contents
    flag=0
    if context['timetables']:
        items={}
        list1=[]
        list2=[]
        for day in week:
            c=0
            for ct in contents['timetables']:
                if day==ct.class_day:
                    if(c==0):
                        list1.append(ct.class_time)
                        c+=1
                    elif(c==1):
                        list2.append(ct.class_time)
                        c+=1
            if(c==0):
                list1.append('None')
                list2.append('None')
            if(c==1):
                list2.append('None')
        context['timetables']=[list1,list2]
    else:
        context['timetables']=None
    return context
    

@is_class_admin
def classconfig(request,c_id):
    class_obj=classroom.objects.get(classid=c_id)
    cnt=0
    if request.POST:
        form=timetableform(request.POST)
        day=request.POST['class_day']
        time=request.POST['class_time']
        time_day=timetable.objects.filter(clsobj=class_obj)
        for classt in time_day:
            if day in classt.class_day:
                cnt+=1
        if(cnt==2):
            messages.error(request,f'You have already added maximum number of classes per Day')
            return redirect('/classroom/'+c_id+'/classconfig')
        else:
            time_table=timetable(clsobj=class_obj,class_day=day,class_time=time)
            time_table.save()
            return redirect('/classroom/'+c_id+'/classconfig')
    else:
        timetables=timetable.objects.filter(clsobj=class_obj)
        form=timetableform()
        content={'form':form,'timetables':timetables,'week':week,'user_class':class_obj}
        context=formtimetable(content)
    return render(request, 'classconfig.html',context)

