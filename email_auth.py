#add to settings.py in elearning
EMAIL_HOST_USER = "adhayayan.scl7maxo@gmail.com"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = "adhayayan7scl"
EMAIL_USE_SSL=False

#add to views.py in userinterface
from django.core.mail import send_mail

#add to views.py in userinterface below cid=rand(6)
send_mail('CLASS CODE','class id='+cid,'adhayayan.scl7maxo@gmail.com',['vishwanath9216@gmail.com'],fail_silently=False)
