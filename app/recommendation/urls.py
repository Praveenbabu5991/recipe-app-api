# recommendations/urls.py
from django.urls import path
from .views import calculate_similarity

urlpatterns = [
    path('calculate_similarity/<int:user_id>/', calculate_similarity, name='calculate-similarity'),
]
