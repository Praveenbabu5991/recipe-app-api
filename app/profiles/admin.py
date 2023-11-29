from django.contrib import admin
from .models import UserProfile,Preference

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Preference)
