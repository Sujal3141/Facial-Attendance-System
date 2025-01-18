import os
import django

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "Attendance_Sys.settings")

# Setup Django
django.setup()

# Now you can import your models and interact with the database
from attendance_app.models import UserProfile

# Example: delete all records from UserProfile
UserProfile.objects.all().delete()