# from django.shortcuts import render

# # Create your views here.
# # recommendations/views.py
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Similarity
# from profiles.models import PsychologicalAnswer
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# from django.conf import settings
# from django.contrib.auth import get_user_model



# @api_view(['GET'])
# def calculate_similarity(request, user_id):
#     # Get answers for the current user
#     user_answers = PsychologicalAnswer.objects.filter(user_id=user_id).values_list('answer', flat=True)

#     # Get all other users' answers
#     user_model = get_user_model()

#     all_users = user_model.objects.exclude(pk=user_id)
#     similarity_scores = []

#     for other_user in all_users:
#         other_user_answers = PsychologicalAnswer.objects.filter(user=other_user).values_list('answer', flat=True)

#         # Calculate TF-IDF vectors for both users' answers
#         tfidf_vectorizer = TfidfVectorizer()
#         tfidf_matrix = tfidf_vectorizer.fit_transform([*user_answers, *other_user_answers])

#         # Calculate cosine similarity between TF-IDF vectors
#         similarity_score = cosine_similarity(tfidf_matrix)[0, 1]

#         # Save similarity score to the database
#         similarity = Similarity(user1=request.user, user2=other_user, similarity_score=similarity_score)
#         similarity.save()

#         similarity_scores.append({
#             'user_id': other_user.id,
#             'username': other_user.username,
#             'similarity_score': similarity_score
#         })

#     return Response(similarity_scores, status=status.HTTP_200_OK)


from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import Similarity
from profiles.models import PsychologicalAnswer
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def calculate_similarity(request, user_id):
    # Convert user_id to integer
    user_id = int(user_id)

    # Get answers for the current user
    user_answers = PsychologicalAnswer.objects.filter(user_id=user_id).values_list('answer', flat=True)

    # Get all other users' answers
    user_model = get_user_model()
    all_users = user_model.objects.exclude(pk=user_id)
    similarity_scores = []

    for other_user in all_users:
        other_user_answers = PsychologicalAnswer.objects.filter(user=other_user).values_list('answer', flat=True)

        # Calculate TF-IDF vectors for both users' answers
        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix = tfidf_vectorizer.fit_transform([*user_answers, *other_user_answers])

        # Calculate cosine similarity between TF-IDF vectors
        similarity_matrix = cosine_similarity(tfidf_matrix)
        similarity_score = similarity_matrix[0, 1]

        # Save similarity score to the database
        similarity = Similarity(user1=request.user, user2=other_user, similarity_score=similarity_score)
        similarity.save()

        similarity_scores.append({
            'user_id': other_user.id,
            'username': other_user.username,
            'similarity_score': similarity_score
        })

    return Response(similarity_scores, status=status.HTTP_200_OK)
