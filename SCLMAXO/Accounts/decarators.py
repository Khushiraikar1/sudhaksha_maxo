from django.http import HttpResponse
from django.shortcuts import redirect
from .models import classroom
def getclasslist(request):
    c=classroom.objects.filter(members=request.user.profile)
    c_list=[]
    for class_room in c:
        c_list.append(class_room.classid)
    return c_list

def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

def is_class_member(allowed_class=[]):
   def decorator(view_func):
       def wrapper_func(request,c_id):
           allowed_class=getclasslist(request)
           if c_id in allowed_class:
               return view_func(request,c_id)
           else:
               return redirect('home')
       return wrapper_func
   return decorator
        