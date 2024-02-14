from django.db import models

# Create your models here.
# profiles/models.py
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='profile')
    bio = models.TextField(blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])
    location = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    similarity_calculation_done = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Preference(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    min_age = models.PositiveIntegerField(null=True, blank=True)
    max_age = models.PositiveIntegerField(null=True, blank=True)
    preferred_gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])

    def __str__(self):
        return f"Preferences for {self.user.username}"


# profiles/models.py
class PsychologicalQuestion(models.Model):
    question_text = models.TextField()

class PsychologicalAnswer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(PsychologicalQuestion, on_delete=models.CASCADE)
    answer = models.TextField()

    def __str__(self):
        return f"Answer by {self.user.username} to question: {self.question.question_text}"
