# profiles/urls.py
from django.urls import path
from .views import user_profile_list_create, user_profile_detail, preference_list_create, preference_detail,psychological_questions_list, psychological_answers_create, psychological_answers_list, psychological_answer_detail

urlpatterns = [
    path('profiles/', user_profile_list_create, name='user-profile-list-create'),
    path('profiles/<int:pk>/', user_profile_detail, name='user-profile-detail'),
    path('preferences/', preference_list_create, name='preference-list-create'),
    path('preferences/<int:pk>/', preference_detail, name='preference-detail'),
    path('psychological/questions/', psychological_questions_list, name='psychological-questions-list'),
    path('psychological/answers/', psychological_answers_list, name='psychological-answers-list'),
    path('psychological/answers/create/', psychological_answers_create, name='psychological-answers-create'),
    path('psychological/answers/<int:pk>/', psychological_answer_detail, name='psychological-answer-detail'),
]


