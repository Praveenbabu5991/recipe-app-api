from django.urls import path
from . import views

app_name='user'


urlpatterns=[
    path("register/",views.register,name="register"),
    path("me/",views.currentUser,name="current"),
    path("updateuser/",views.updateUser,name="updateUser"),

]