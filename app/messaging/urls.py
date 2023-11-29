# messaging/urls.py
from django.urls import path
from .views import conversation_list_create, conversation_detail, message_list_create, message_detail

urlpatterns = [
    path('conversations/', conversation_list_create, name='conversation-list-create'),
    path('conversations/<int:pk>/', conversation_detail, name='conversation-detail'),
    path('messages/', message_list_create, name='message-list-create'),
    path('messages/<int:pk>/', message_detail, name='message-detail'),
]
