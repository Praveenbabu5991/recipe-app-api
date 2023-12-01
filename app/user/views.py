from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.hashers import make_password
from .serializers import SignUpSerializer,UserSerializer

from rest_framework.permissions import IsAuthenticated

# from django.contrib.auth.models import User



from django.contrib.auth import get_user_model
User = get_user_model()

# @api_view(['POST'])
# def register(request):

#     data = request.data

#     serializer=SignUpSerializer(data=data)
#     if serializer.is_valid():
#         if not User.objects.filter(username=data['email']).exists():
#             serializer=User.objects.create(
#                 first_name=data['first_name'],
#                 last_name=data['last_name'],
#                 username=data['email'],
#                 email=data['email'],
#                 password=make_password(data['password'])
#             )
#             return Response({
#                 'message': 'User registered'},
#                 status=status.HTTP_200_ok
#             )
#         else:
#             return Response({
#                 'error':'User already exists'},
#                 status=status.HTTP_400_BAD_REQUEST
#                 )
#     else:
#         return Response(serializer.errors)



@api_view(['POST'])
def register(request):
    print("++++++++++++++++++++++++++++++++userfields++++++++++1.1",User._meta.fields)

    data = request.data

    serializer = SignUpSerializer(data=data)
    print("++++++++++++++++++++++++++++++++++1.1",serializer)
    if serializer.is_valid():
        if not User.objects.filter(username=data['email']).exists():
            # Create a new User instance using the validated data from the serializer
            new_user = User.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                username=data['email'],
                email=data['email'],
                password=make_password(data['password'])
            )
            return Response({
                'message': 'User registered'},
                status=status.HTTP_200_OK
            )
        else:
            return Response({
                'error': 'User already exists'},
                status=status.HTTP_400_BAD_REQUEST
            )
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def currentUser(request):
    user= UserSerializer(request.user)
    return Response(user.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUser(request):
    user =request.user

    data =request.data

    user.first_name=data['first_name']
    user.last_name=data['last_name']
    user.username=data['email']
    user.email=data['email']

    if data['password'] != "":
        user.password=make_password(data['password'])

    user.save()
    serializer=UserSerializer(user, many=False)
    return Response(serializer.data)
