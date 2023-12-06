# profiles/serializers.py
from rest_framework import serializers
from .models import UserProfile, Preference, PsychologicalQuestion, PsychologicalAnswer

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

        extra_kwargs = {
            'profile_picture': {'required': False}
        }

class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preference
        fields = '__all__'


# profiles/serializers.py
class PsychologicalQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PsychologicalQuestion
        fields = '__all__'

class PsychologicalAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PsychologicalAnswer
        fields = '__all__'
