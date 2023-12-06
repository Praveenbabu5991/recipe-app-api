from django.contrib import admin
from .models import UserProfile,Preference,PsychologicalQuestion,PsychologicalAnswer

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Preference)
admin.site.register(PsychologicalQuestion)
admin.site.register(PsychologicalAnswer)
