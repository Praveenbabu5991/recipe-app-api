# messaging/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer

# View to list all conversations or create a new conversation
@api_view(['GET', 'POST'])
def conversation_list_create(request):
    if request.method == 'GET':
        # Retrieve all conversations
        conversations = Conversation.objects.all()
        serializer = ConversationSerializer(conversations, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # Create a new conversation
        serializer = ConversationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View to retrieve details of a specific conversation
@api_view(['GET'])
def conversation_detail(request, pk):
    try:
        # Retrieve the conversation with the given primary key
        conversation = Conversation.objects.get(pk=pk)
    except Conversation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ConversationSerializer(conversation)
    return Response(serializer.data)

# View to list all messages or create a new message
@api_view(['GET', 'POST'])
def message_list_create(request):
    if request.method == 'GET':
        # Retrieve all messages
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # Create a new message
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View to retrieve details of a specific message
@api_view(['GET'])
def message_detail(request, pk):
    try:
        # Retrieve the message with the given primary key
        message = Message.objects.get(pk=pk)
    except Message.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = MessageSerializer(message)
    return Response(serializer.data)

# View to send a new message
@api_view(['POST'])
def send_message(request):
    # Create and send a new message
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View to retrieve messages for a specific conversation
@api_view(['GET'])
def retrieve_messages(request, conversation_id):
    try:
        # Retrieve the conversation with the given ID
        conversation = Conversation.objects.get(pk=conversation_id)
        # Retrieve all messages for this conversation
        messages = conversation.messages.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
    except Conversation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
