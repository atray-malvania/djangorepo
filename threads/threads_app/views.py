from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from threads_app.models import *
from threads_app.forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.
@login_required
def index(request):
    story = Story.objects.all()
    comments = Comments.objects.all()
    indexreturn = {'stories':story,'comments':comments}
    return render(request,'threads_app/index.html',context=indexreturn)

def chat(request):
    user = UserProfile.objects.all()
    users = {'User1':user[0],'User2':user[1]}
    return render(request, 'threads_app/chat.html',context=users)

def registraion(request):
    
    if(request.method == 'POST'):
        userform = loginForm(data=request.POST)
        userprofileform = uForm(data=request.POST)
        print('1')
        # user = User()
        if userform.is_valid():
            print('2')
            try:
                u=userform.save(commit=True)
                userp = UserProfile()
                userprofileform.save(commit=False)
                print('3')
                userp.user = u
                userp.phone = userprofileform.cleaned_data['phone']
                userp.save()
                print('4')
            
                # messages.success(request, 'Registration successful!')
                messages.success(request,'Registration Successful')
                print('Success')
                return index(request)
            except Exception as e:
                print(e)
        else:
            print('Something went wrong')   
    else:
        userform = loginForm() 
        userprofileform = uForm() 
        print('d')  
    
    return render(request,'threads_app/register.html',{'form1':userform,'form2':userprofileform})


def user_login(request):
    
    if request.method == "POST":
        uname = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=uname,password=password)
        
        if user:
            print('Success')
            login(request,user=user)
            return HttpResponseRedirect(reverse(index))
    
    
    return render(request, 'threads_app/login.html',{})