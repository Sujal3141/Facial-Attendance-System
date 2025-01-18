from django.db import models

class UserProfile(models.Model):
    user_id = models.CharField(max_length=10)
    user_name = models.CharField(max_length=100)
    user_img = models.ImageField(upload_to='user_images')  
    user_email = models.EmailField()
    user_city = models.CharField(max_length=50)
    user_phone_no = models.CharField(max_length=100)
    user_zip_code = models.IntegerField()
    user_Attendance_Count= models.IntegerField(default=0,blank=True)


