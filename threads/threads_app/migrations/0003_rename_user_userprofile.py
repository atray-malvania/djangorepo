# Generated by Django 4.2.5 on 2023-10-05 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threads_app', '0002_remove_story_story_comment_comments_story'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserProfile',
        ),
    ]
