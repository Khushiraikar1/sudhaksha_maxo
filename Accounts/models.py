from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .randgenrator import rand
# Create your models here.
import datetime

# Create your models here.
ROLE=(("TEACHER","TEACHER"),
       ("STUDENT","STUDENT"))
USER_FIELD=(("ENGINEERING","ENGINEERING"),
            ("MEDICAL","MEDICAL"),
            ("OTHER","OTHER"))
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    role=models.CharField(max_length=15,choices=ROLE,default="STUDENT")
    Uid=models.CharField(max_length=20,null=True)
    image=models.CharField(max_length=255,default=None,null=True)
    user_field=models.CharField(max_length=20,choices=USER_FIELD,null=True)
    date_joined=models.DateField('date_joined',default=datetime.date.today)

    def __str__(self):
           return self.user.username

class classroom(models.Model):
       class_name=models.CharField(max_length=50,null=True)
       class_sec=models.CharField(max_length=50,null=True)
       class_subject=models.CharField(max_length=50,null=True)
       classid=models.CharField(max_length=15,null=True)
       admin=models.ForeignKey(User,on_delete=models.CASCADE)
       c_url=models.URLField(default=None,null=True)
       members=models.ManyToManyField(profile)

       def __str__(self):
              return self.class_name

       def get_abs_url(self):
              return reverse('classroom',kwargs={'c_id':self.classid})
       
       def is_admin(self):
              return self.admin


    