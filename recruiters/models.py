from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# recruiters/models.py
class RecruiterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="recruiter_profile")
    job_title = models.CharField(max_length=255, blank=True)
