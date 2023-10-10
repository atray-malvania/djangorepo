# Generated by Django 4.2.5 on 2023-10-09 04:55

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('threads_app', '0006_userprofile_gender_alter_story_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='story_media',
            field=models.FileField(blank=True, default=None, null=True, upload_to='profile/'),
        ),
        migrations.AlterField(
            model_name='story',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 10, 9, 4, 55, 42, 988640), null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_portfolio',
            field=models.URLField(blank=True, default='http://127.0.0.1:8000/', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_uuid',
            field=models.UUIDField(default=uuid.UUID('f6c43e76-9e5d-49c8-9bf0-fe4ed8c7f5ef'), editable=False),
        ),
    ]