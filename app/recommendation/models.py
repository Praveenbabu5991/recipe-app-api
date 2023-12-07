
# Create your models here.
# recommendations/models.py
from django.db import models
from django.conf import settings

class Similarity(models.Model):
    user1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user2')
    similarity_score = models.FloatField()

    def __str__(self):
        return f"Similarity between {self.user1.username} and {self.user2.username}: {self.similarity_score}"
