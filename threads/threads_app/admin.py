from django.contrib import admin
from threads_app.models import UserProfile, Message, Comments, Story

# Register your models here.

# to customise admin interface for the user model
class UserAdmin(admin.ModelAdmin):
    model = UserProfile
    
    
class MessageAdmin(admin.ModelAdmin):
    model = Message
    
    
class CommentsAdmin(admin.ModelAdmin):
    model = Comments
    list_filter = ["Story"]
    list_display = ["Story"]

class StoryAdmin(admin.ModelAdmin):
    model = Story   
    list_filter = ["story_title"]
    list_display = ["story_title"] 
    
admin.site.register(UserProfile)
admin.site.register(Message)
admin.site.register(Comments)
admin.site.register(Story, StoryAdmin)
