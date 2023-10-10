from django.db import models
from django.contrib.auth.models import User 
import uuid
from datetime import datetime

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    phone = models.IntegerField()
    # user_id = models.AutoField(null=True)
    user_active = models.BooleanField(verbose_name='isActive',default=True)
    user_profilepic = models.FilePathField(path = "media/", match = ".jpeg",recursive=False,default=None,null=True,blank=True)
    user_portfolio = models.URLField(blank=True,null=True,default='http://127.0.0.1:8000/')
    user_uuid = models.UUIDField(default=uuid.uuid4(),editable=False)
    
    GENDER = [
        ('M', 'male'),
        ('F','female')
    ]
    gender = models.CharField(max_length=1,choices=GENDER, null=True, blank=True)
    
    
    def __str__(self) :
        return self.user.username
    
class Story(models.Model):
    story_title = models.CharField(unique=True, max_length=15)
    # slug = models.SlugField(max_length=256, blank=True, null=True)
    story_content = models.TextField()
    created_by = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    date = models.DateField(null=True,default=datetime.now())
    story_media = models.FileField(upload_to='profile/',default=None, null=True, blank=True)
    
    # Automatically generatee slug from story_title
    # def save(self, *args, **kwargs):
    #     self.slug  = self.story_title.lower().replace(' ','-')
    #     super().save(*args, **kwargs)
    
    def __str__(self):
        return self.story_title
    
class Comments(models.Model):
    created_by = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    date = models.DateField()
    comment = models.CharField( max_length=15)
    story = models.ForeignKey(Story,on_delete=models.CASCADE,default=None)
    
    def __str__(self):
        return self.comment
    
class Message(models.Model):
    from_message = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    msg = models.CharField( max_length=15)
    date = models.DateTimeField(null=True)
    
    
    def __str__(self):
        return self.msg

    
    
    