# recommendation/serializers.py

from rest_framework import serializers
from .models import Similarity
class SimilaritySerializer(serializers.Serializer):
    # Define your serializer fields and logic here
      class Meta:
        model = Similarity
        fields = '__all__'
