# Generated by Django 5.1.4 on 2025-01-12 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_app', '0002_alter_userprofile_user_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_Attendance_Count',
            field=models.IntegerField(default=0),
        ),
    ]
