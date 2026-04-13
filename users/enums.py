from django.db import models


class UserRole(models.TextChoices):
    CANDIDATE = "candidate", "Candidate"
    RECRUITER = "recruiter", "Recruiter"
    ADMIN = "admin", "Admin"
