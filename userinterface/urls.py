from django.urls import path
from . import views
urlpatterns=[
    path('home',views.home,name='home'),
    path('<int:idk>',views.some,name='any'),
    path('catalogue',views.catalogue,name='catalogue'),
    path('help',views.help,name='help'),
    path('createclass',views.createclass,name="create"),
    path('classroom',views.class_room,name="classroom-home"),
    path('classroom/<str:c_id>',views.CLASSROOM,name="classroom"),
    path('joinclass',views.joinclass,name="join"),
    path('classroom/<str:c_id>/admin',views.classadmin,name="admin-page"),
    path('classroom/<str:c_id>/classconfig',views.classconfig,name="class-time"),
    path('classroom/<str:c_id>/people',views.people,name="people"),
    path('classroom/<str:c_id>/attendance',views.class_attend,name="attendance"),
    path('classroom/<str:c_id>/submit',views.attend_submit,name="submit-attendance"),

]