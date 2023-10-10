from django.contrib import admin
from django.urls import path
from threads_app.views import *

app_name = 'threads_app'

urlpatterns = [
    path('index',index,name='index'),
    path('chat',chat,name = 'chat'),
    path('register',registraion,name = 'register'),
    path('login',user_login, name= 'login')
]
