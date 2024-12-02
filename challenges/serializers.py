
from rest_framework import serializers
from .models import Challenges, Categories, Hints,ChallengesResults

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class HintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hints
        fields =  ['id', 'hint_text'] 

from .models import ChallengesResults

class ChallengeResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChallengesResults
        fields = '__all__'


class ChallengeSerializer(serializers.ModelSerializer):
    category = CategorySerializer() 
    hints = HintSerializer(many=True, read_only=True)
    solved = serializers.SerializerMethodField()
    class Meta:
        model = Challenges
        fields  = ['id', 'title', 'description', 'link', 'timer', 'flag', 'level','nc', 'category', 'points', 'hints','solved']
    def get_solved(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated:
           try:
            
            challenge_result = ChallengesResults.objects.get(user=user, challenge=obj)
            return challenge_result.solved
           except ChallengesResults.DoesNotExist:
            return False
        else :
            return False
