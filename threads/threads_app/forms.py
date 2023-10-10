from django import forms
from threads_app.models import UserProfile
from django.contrib.auth.models import User 

class loginForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username','email','password')
    # fields = '__all__' in case all fields are required from model
    
class uForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        exclude = ['user','user_active','user_profilepic','user_portfolio','gender']