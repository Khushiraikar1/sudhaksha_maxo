from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile,classroom,timetable,attendance

class Registrationform(UserCreationForm):
	email=forms.EmailField()
	class Meta:
		model=User
		fields=['username','email','password1','password2']
class Register(forms.ModelForm):
	email=forms.EmailField()
	class Meta:
		model=User
		fields=['username','email']
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		#self.fields['username'].widget.attrs['disabled']=''

class Profileform(forms.ModelForm):
	class Meta:
		model=profile
		fields=['role','image','user_field']
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		#self.fields['Uid'].widget.attrs['disabled']=''
		self.fields['image'].widget.attrs['placeholder'] = 'Image'

class Classform(forms.ModelForm):
	class Meta:
		model=classroom
		fields=['class_name','class_sec','class_subject']
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['class_name'].widget.attrs['name'] ='class_name'
		self.fields['class_sec'].widget.attrs['name']='section'
		self.fields['class_subject'].widget.attrs['name'] = 'subject'

class timetableform(forms.ModelForm):
	class Meta:
		model=timetable
		fields=['class_day','class_time']
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['class_time'].widget.attrs['input_type'] ='time'

class attendanceform(forms.ModelForm):
	class Meta:
		model=attendance
		fields=['attendance_time']
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['attendance_time'].widget.attrs['placeholder'] ='YYYY-MM-DD HH:MM'
		
