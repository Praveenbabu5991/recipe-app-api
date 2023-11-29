# profiles/urls.py
from django.urls import path
from .views import user_profile_list_create, user_profile_detail, preference_list_create, preference_detail

urlpatterns = [
    path('profiles/', user_profile_list_create, name='user-profile-list-create'),
    path('profiles/<int:pk>/', user_profile_detail, name='user-profile-detail'),
    path('preferences/', preference_list_create, name='preference-list-create'),
    path('preferences/<int:pk>/', preference_detail, name='preference-detail'),
]
