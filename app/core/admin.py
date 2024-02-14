from django.contrib import admin


# Register your models here.
from .models import User

# admin.site.register(UserManager)
admin.site.register(User)
