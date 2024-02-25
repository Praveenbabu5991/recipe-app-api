# messaging/urls.py
from django.urls import path
from .views import conversation_list_create, conversation_detail, message_list_create, message_detail,send_message,retrieve_messages  

urlpatterns = [
    path('conversations/', conversation_list_create, name='conversation-list-create'),
    path('conversations/<int:pk>/', conversation_detail, name='conversation-detail'),
    path('messages/', message_list_create, name='message-list-create'),
    path('messages/<int:pk>/', message_detail, name='message-detail'),
    path('send_message/', send_message, name='send-message'),  # URL for sending a message
    path('retrieve_messages/<int:conversation_id>/', retrieve_messages, name='retrieve-messages'),  # URL for retrieving messages for a conversation

]
